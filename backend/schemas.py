from pydantic import BaseModel


class UserAuthRequest(BaseModel):
    code: str
    state: str
