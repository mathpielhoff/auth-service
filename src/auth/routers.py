from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session


from src.auth.model.RegisterRequest import RegisterRequest
from src.auth.model.User import User
from src.auth.model.LoginRequest import LoginRequest
from src.auth.utils import hash_password, verify_password

from shared_lib.utils.jwt_utils import decode_jwt, create_access_token
from shared_lib.utils.db_utils import Base, get_db

auth_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@auth_router.post("/login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first() 
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if not user or not verify_password(request.password, user.hashed_password):
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

@auth_router.post("/register/")
def create_user(request : RegisterRequest, db: Session = Depends(get_db)): 
    hashed_password=hash_password(request.password)
    user = User(username=request.username, email=request.email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user