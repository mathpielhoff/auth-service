from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.auth.routers import auth_router
from dotenv import load_dotenv
from shared_lib.utils.db_utils import init_db


# Charger les variables d'environnement
load_dotenv()
# Initialiser la base de données lors du lancement du microservice
init_db()

app = FastAPI(title="Auth Service", version="1.0")

# Ajouter le middleware CORS
origins = [
    "http://localhost",  # Permet d'accéder depuis ton frontend local
    "http://localhost:5173",  # Permet d'accéder depuis un autre port, si ton frontend tourne sur 8080
    "https://tonfrontend.com",  # Remplace avec l'URL de ton frontend en production
    # Ajoute d'autres URL si nécessaire
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Liste des URL autorisées
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Autorise toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autorise tous les headers
)

# Inclure le routeur d'authentification
app.include_router(auth_router, prefix="/auth", tags=["auth"])
