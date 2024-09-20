from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base
from ..core.config import settings

# URL de connection à la base de données
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Créer l'engine pour la base de données
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Créer une session locale pour interagir avec la base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# fonction de dépendance pour obtenir une session SQLAlchemy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

# Initialisation des tables
def init_db():
    # Créer toutes les tables
    Base.metadata.create_all(bind=engine)