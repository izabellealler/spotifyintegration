import requests
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse

from backend.requests.playlist import get_playlist_items

router = APIRouter()


@router.get('/filter')
def read_filter(access_token: str = Query(...)):
    try:
        informations = get_playlist_items(access_token)
        ids = ",".join(item['track']['id'] for item in informations['items'])
        return RedirectResponse(url=f"/features/filter?access_token={access_token}&ids={ids}")
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
