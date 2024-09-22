from pydantic_core._pydantic_core import ValidationError
from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.db.session import get_db
from app.services.user_service import (
    create_user_service,
    get_user_by_email_service
)
router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def show_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/", response_class=HTMLResponse)
async def register_user(
    request: Request,
    username: str = Form(...),
    age: int = Form(...),
    initial_weight: float = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
    db: Session = Depends(get_db)
):
    # Vérifier si les mots de passe correspondent
    if password != confirm_password:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Les mots de passe ne correspondent pas."})
    
    # Vérifier si l'utilisateur existe déjà
    try:
        get_user_by_email_service(db, email)
        return templates.TemplateResponse("register.html", {"request": request, "error": "Cet email est déjà utilisé."})
    except ValueError as e:
        if str(e) == "User not found":
            pass  # L'utilisateur n'existe pas, on peut continuer
        else:
            return templates.TemplateResponse("register.html", {"request": request, "error": str(e)})
    
    # Créer un nouvel utilisateur
    user = UserCreate(
        username=username,
        email=email,
        age=age,
        initial_weight=initial_weight,
        password=password
    )
    try:
        create_user_service(db, user)
        return templates.TemplateResponse("register.html", {"request": request, "success": "Votre compte a été créé avec succès."})
    except ValidationError as e:
        return templates.TemplateResponse("register.html", {"request": request, "error": str(e)})
    except ValueError as e:
        return templates.TemplateResponse("register.html", {"request": request, "error": str(e)})
    

