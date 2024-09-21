from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from sqlalchemy.orm import Session
from app.core.security import get_password_hash, verify_password
from app.db.session import get_db
from app.services.user_service import get_user_in_db_service

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/")
async def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        user = get_user_in_db_service(db, email)
    except ValueError as e:
        if str(e) == "User not found":
            return templates.TemplateResponse("login.html", {"request": request, "error": "Email ou mot de passe incorrect."})
        else:
            return templates.TemplateResponse("login.html", {"request": request, "error": str(e)})
        
    if not verify_password(password, user.hashed_password):
        return templates.TemplateResponse("login.html", {"request": request, "error": "Email ou mot de passe incorrect."})

    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie(key="user_id", value=str(user.id))
    return response