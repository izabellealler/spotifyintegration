from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from backend.routers import auth, features, playlist, search

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(search.router, prefix="/search", tags=["search"])
app.include_router(playlist.router, prefix="/playlist", tags=["playlist"])
app.include_router(features.router, prefix="/features", tags=["features"])


@app.get("/")
def read_root():
    return RedirectResponse(url="/auth/login")
