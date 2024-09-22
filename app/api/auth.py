from datetime import timedelta
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.core.config import settings
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.token import Token
from app.services.auth_service import (
    authenticate_user, create_access_token, credentials_exception
)

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@auth_router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
    ):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise credentials_exception
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
