from pydantic import BaseModel

class LoginResponse(BaseModel):
    username: str
    tenant_id: int
    role : str
