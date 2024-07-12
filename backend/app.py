from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from backend.routers import auth

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
# app.include_router(search.router, prefix="/search", tags=["search"])


@app.get("/")
def read_root():
    return RedirectResponse(url="/auth/login")
