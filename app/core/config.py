import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    # Configuration générale
    APP_NAME:str = "Suivi de Repas"
    ENVIRONMENT:str = os.getenv("ENVIRONMENT", "production")
    DATABASE_URL: str
    DATABASE_URL_TEST: str = "sqlite:///./test.db"
    # Configuration base de données en fonction de l'environnement
    if ENVIRONMENT == 'production':
        DATABASE_URL = os.getenv("DATABASE_URL")
    else:
        DATABASE_URL = DATABASE_URL_TEST  # Base de données par défaut


    # Configuration de sécurité
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_default_secret_key")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)

    model_config = {
        "env_file" : ".env"
    }

# Crée une instance de Settings pour être utilisée dans toute l'application
settings = Settings()
