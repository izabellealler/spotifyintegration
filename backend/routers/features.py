import requests
from fastapi import APIRouter, HTTPException, Query

from backend.requests.features import get_features

router = APIRouter()


@router.get('/filter')
def read_filter(access_token: str = Query(...), ids: str = Query(...)):
    try:
        informations = get_features(access_token=access_token, ids=ids)
        return informations
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
