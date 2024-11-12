from datetime import datetime, timedelta
import os
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
from src.auth.model.LoginResponse import LoginResponse
from src.auth.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

# Configuration pour le mot de passe et JWT
# Récupérer les configurations


# Contexte pour le hashing des mots de passe
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Simuler un utilisateur
fake_user_db = {
    "therapist1": {
        "username": "therapist1",
        "hashed_password": pwd_context.hash("password123"),
        "tenant_id":1,
        "role": "therapist",
    }
}

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    user = fake_user_db.get(username)
    if not user or not verify_password(password, user["hashed_password"]):
        return None
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_jwt(token: str) -> LoginResponse:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        tenant_id: int = payload.get("tenantId")
        print(payload)
        if username is None or role is None or tenant_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token payload invalid",
            )
        return LoginResponse(username=username, tenant_id=tenant_id, role=role)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is invalid or expired",
        )