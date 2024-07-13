import requests
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse

from backend.requests.search import get_search
from backend.utils.saveexcel import save_excel

router = APIRouter()


@router.get('/filter')
def read_filter(access_token: str = Query(...)):
    try:
        informations = get_search(access_token)
        ids = ",".join(track.get('id') for track in informations['tracks']['items'])
        return RedirectResponse(url=f"/features/filter?access_token={access_token}&ids={ids}")
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
