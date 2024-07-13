import requests
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse

from backend.requests.auth import (
    get_auth_url,
    get_token,
)
from backend.settings import settings

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
        if bool(settings.STATUS):
            redirect_url = f"/playlist/filter?access_token={access_token}"
        else:
            redirect_url = f"/search/filter?access_token={access_token}"
        return RedirectResponse(url=redirect_url)
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
