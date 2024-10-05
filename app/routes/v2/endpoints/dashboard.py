from datetime import date, time
from pydantic_core._pydantic_core import ValidationError
from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.schemas.meal import MealCreate
from starlette.responses import RedirectResponse
from app.db.session import get_db
from app.services.user_service import (
    get_user_by_id_service, get_users_service
)
from app.services.meal_service import (
    get_meals_by_user_service, create_meal_service
)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates/angular")

@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    to_template = {
        "request": request,
        "username": request.cookies.get("username"),
    }
    return templates.TemplateResponse("dashboard.html", to_template)

@router.post("/", response_class=HTMLResponse)
async def add_meal(
    request: Request,
    username: str = Form(...),
    date: date = Form(...),
    time: time = Form(...),
    type: str = Form(...),
    db: Session = Depends(get_db)
):
    if not username:
        return templates.TemplateResponse("login.html", {"request": request})
    try:
        get_user_by_id_service(db, int(username))
    except ValueError as e:
        if str(e) == "User not found":
            return templates.TemplateResponse("login.html", {"request": request})
        else:
            return templates.TemplateResponse("dashboard.html", {"request": request, "error": str(e)})
    meal = MealCreate(
        user_id=username,
        date=date,
        time=time,
        type=type
    )
    try:
        create_meal_service(db, meal)
        response = RedirectResponse(url="/dashboard", status_code=303)
        response.set_cookie(key="user_id", value=str(username))
        return response
    except ValidationError as e:
        return templates.TemplateResponse("dashboard.html", {"request": request, "error": str(e)})
