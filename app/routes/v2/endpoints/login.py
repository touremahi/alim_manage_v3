from datetime  import timedelta

from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.core.config import settings
from app.schemas import LoginData
from app.core.security import verify_password
from app.db.session import get_db
from app.services.user_service import get_user_in_db_service

router = APIRouter()

templates = Jinja2Templates(directory="app/templates/angular")

@router.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/")
async def login(
    request: Request,
    data: LoginData,
    db: Session = Depends(get_db)
):
    error_message = "Utilisateur ou mot de passe incorrect."
    try:
        user = get_user_in_db_service(db, data.email)
    except ValueError as e:
        if str(e) == "User not found":
            raise HTTPException(status_code=404, detail=error_message)
        else:
            raise HTTPException(status_code=404, detail=error_message)
        
    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=404, detail=error_message)
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    # response = RedirectResponse(url="/dashboard", status_code=303)
    # response.set_cookie(key="access_token", value=access_token)
    return {
        "message" : "Login successful",
        "access_token": access_token,
        "token_type": "bearer",
    }