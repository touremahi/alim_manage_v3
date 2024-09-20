from datetime import timedelta

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ..schemas.token import TokenData
from ..schemas.user import UserCreate, UserOut, UserInDB
from .user_service import (
    get_user_by_email_service, get_user_in_db_service
)
from ..core.security import (
    verify_password, create_access_token, verify_token
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_in_db_service(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token_service(data: dict, expires_delta: timedelta = None):
    return create_access_token(data, expires_delta)

async def get_current_user(db: Session, token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        return None
    username: str = payload.get("sub")
    if not username:
        return None
    user = get_user_in_db_service(db, username)
    if not user:
        return None
    return user

async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if not current_user:
        return None
    return current_user