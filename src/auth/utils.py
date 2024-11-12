from passlib.context import CryptContext
from shared_lib.models.LoginResponse import LoginResponse

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