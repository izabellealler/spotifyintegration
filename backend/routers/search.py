import requests
from fastapi import APIRouter, HTTPException, Query

from backend.requests.search import get_search

router = APIRouter()


@router.get('/filter')
def read_filter(access_token: str = Query(...)):
    try:
        informations = get_search(access_token)
        return informations
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
