from typing import Dict

import requests

from backend.settings import settings


def get_search(access_token: str) -> Dict:
    response = requests.get(
        'https://api.spotify.com/v1/search',
        headers={
            'Authorization': f'Bearer {access_token}',
        },
        params={
            "q": f"{settings.SPOTIPY_GENRES}",
            "type": ["track"],
            "market": "BR",
            "limit": 50,
          }
    )
    response.raise_for_status()
    return response.json()
