from fastapi import FastAPI
from src.auth.routers import auth_router

app = FastAPI(title="Auth Service", version="1.0")

# Inclure le routeur d'authentification
app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Auth Service is running"}
