import base64
import secrets
from typing import Dict
from urllib.parse import parse_qs, urlencode, urlparse

import requests

from backend.settings import settings


def get_spotify_auth_url() -> str:
    state_expected = secrets.token_urlsafe(16)
    data = {
            "client_id": settings.SPOTIPY_CLIENT_ID,
            "response_type": "code",
            "redirect_uri": settings.SPOTIPY_REDIRECT_URI,
            "scope": settings.SPOTIPY_SCOPE,
            "state": f"{state_expected}",
        }
    auth_url = "https://accounts.spotify.com/authorize?" + urlencode(data)
    return auth_url


def get_code(auth_url: str):
    parsed_url = urlparse(auth_url)
    query_params = parse_qs(parsed_url.query)
    code = query_params.get('code', [None])[0]
    return code


def get_spotify_token(code: str) -> Dict:
    auth_header = base64.b64encode(f"{settings.SPOTIPY_CLIENT_ID}:{settings.SPOTIPY_CLIENT_SECRET}".encode()).decode()
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
        'Authorization': f'Basic {auth_header}'
        },
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": settings.SPOTIPY_REDIRECT_URI,
        },
    )
    response.raise_for_status()
    return response.json()
