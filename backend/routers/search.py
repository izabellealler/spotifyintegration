import requests
from fastapi import APIRouter, HTTPException, Query

from backend.myapi import get_informations

router = APIRouter()


@router.get('/filter')
def search_for_item(access_token: str = Query(...)):
    try:
        informations = get_informations(access_token)
        return informations
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
