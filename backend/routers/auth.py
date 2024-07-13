import requests
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse

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
        path = input("search or playlist: ")
        return RedirectResponse(url=f"/{path}/filter?access_token={access_token}")
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
