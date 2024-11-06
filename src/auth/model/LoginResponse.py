from pydantic import BaseModel

class LoginResponse(BaseModel):
    username: str
    hashed_password: str
    role : str
