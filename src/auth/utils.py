from passlib.context import CryptContext
from shared_lib.models.LoginResponse import LoginResponse

# Configuration pour le mot de passe et JWT
# Récupérer les configurations


# Contexte pour le hashing des mots de passe
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plan_password) -> str:
    return pwd_context.hash(plan_password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

