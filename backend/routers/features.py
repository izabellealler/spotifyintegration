import requests
from fastapi import APIRouter, HTTPException, Query

from backend.requests.features import get_features
from backend.settings import settings
from backend.utils.saveexcel import save_excel

router = APIRouter()


@router.get('/filter')
def read_filter(access_token: str = Query(...), ids: str = Query(...)):
    try:
        informations = get_features(access_token=access_token, ids=ids)
        if bool(settings.STATUS):
            save_excel('playlist_features.xlsx', informations.get("audio_features"))
        else:
            save_excel('search_features.xlsx', informations.get("audio_features"))
        raise HTTPException(status_code=200, detail='OK - The request has succeeded.')
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
