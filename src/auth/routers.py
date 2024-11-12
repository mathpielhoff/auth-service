from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from src.auth.model.LoginResponse import LoginResponse
from src.auth.model.LoginRequest import LoginRequest
from src.auth.utils import authenticate_user, create_access_token, decode_jwt

auth_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@auth_router.post("/login")
async def login(request: LoginRequest):
    user = authenticate_user(request.username, request.password)
    user = LoginResponse(
        username=user["username"],
        tenant_id=user["tenant_id"],
        role=user["role"]
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(data={"sub": user.username, "tenantId":user.tenant_id, "role":user.role})
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.get("/whoami")
async def whoami(token: str = Depends(oauth2_scheme)):
    user = decode_jwt(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    return {"username": user.username, "role": user.role}