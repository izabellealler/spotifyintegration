from typing import Dict

import requests


def get_features(access_token: str, ids: str) -> Dict:
    response = requests.get(
        'https://api.spotify.com/v1/audio-features',
        headers={
            'Authorization': f'Bearer {access_token}',
        },
        params={
            "ids": ids,
        }
    )
    response.raise_for_status()
    return response.json()
