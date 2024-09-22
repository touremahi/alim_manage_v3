from datetime import timedelta

from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from ..schemas.token import TokenData
from ..schemas.user import UserInDB
from app.db.session import get_db
from .user_service import (
    get_user_by_username_service, get_user_in_db_service
)
from ..core.security import (
    verify_password, create_access_token, verify_token
)

def is_api_request(request: Request):
    if request.headers.get("accept") == "application/json":
        return True
    return False

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect username or password",
    headers={"WWW-Authenticate": "Bearer"},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def get_user(db: Session, username: str):
    try:
        return get_user_by_username_service(db, username)
    except:
        return False

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token_service(data: dict, expires_delta: timedelta = None):
    return create_access_token(data, expires_delta)

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = verify_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = get_user(db, username=token_data.username)
    if not user:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=400, detail="Inactive user")
    
    return current_user

async def get_current_web_user(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        return None
    try:
        payload = verify_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = get_user(db, username=token_data.username)
    if not user:
        raise credentials_exception
    return user

async def get_current_web_active_user(current_user: UserInDB = Depends(get_current_web_user)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Inactive user")

    return current_user
