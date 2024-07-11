import requests
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse

from backend.security import (
    get_spotify_auth_url,
    get_spotify_token,
)

router = APIRouter()


@router.get('/login')
def login_for_auth_url():
    auth_url = get_spotify_auth_url()
    return RedirectResponse(url=auth_url)


@router.get('/callback')
def get_token(code: str = Query(...)):
    try:
        token = get_spotify_token(code)
        return token
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
