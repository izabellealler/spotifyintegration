import requests
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse
from backend.settings import settings
from backend.requests.auth import (
    get_auth_url,
    get_token,
)

router = APIRouter()


@router.get('/login')
def read_login():
    try:
        auth_url, code = get_auth_url()
        return RedirectResponse(url=auth_url)
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())


@router.get('/callback')
def read_callback(code: str = Query(...)):
    try:
        token = get_token(code)
        access_token = token.get('access_token')
        search_url= f"/search/filter?access_token={access_token}"
        playlist_url= f"/playlist/filter?access_token={access_token}"
        redirect_url = playlist_url if settings.STATUS else search_url
        return RedirectResponse(url=redirect_url)
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
