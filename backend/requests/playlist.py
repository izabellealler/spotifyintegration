from typing import Dict

import requests

from backend.settings import settings


def get_playlist_items(access_token: str) -> Dict:
    response = requests.get(
        f'https://api.spotify.com/v1/playlists/{settings.SPOTIPY_PLAYLIST_ID}/tracks',
        headers={
            'Authorization': f'Bearer {access_token}',
        },
        params={
            "playlist_id": f"{settings.SPOTIPY_PLAYLIST_ID}",
            "fields": "items.track.id",
            "market": "BR",
            "limit": 100,
            "additional_types": "track",
        }
    )
    response.raise_for_status()
    return response.json()
