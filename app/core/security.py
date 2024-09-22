from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from .config import settings
from passlib.context import CryptContext

# Fonction pour hacher un mot de passe
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Générer un token JWT
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

# Vérifier un token JWT
def verify_token(token: str):
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    return payload

# Verifier un mot de passe
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Hacher un mot de passe
def get_password_hash(password):
    return pwd_context.hash(password)
