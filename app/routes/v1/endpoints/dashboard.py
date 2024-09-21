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
    get_user_by_id_service
)
from app.services.meal_service import (
    get_meals_by_user_service, create_meal_service
)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return templates.TemplateResponse("login.html", {"request": request})
    username = get_user_by_id_service(db, int(user_id)).username
    meals = get_meals_by_user_service(db, user_id)

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "meals": meals,
            "username": username
        }
    )

@router.post("/", response_class=HTMLResponse)
async def add_meal(
    request: Request,
    username: str = Form(...),
    date: date = Form(...),
    time: time = Form(...),
    type: str = Form(...),
    db: Session = Depends(get_db)
):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return templates.TemplateResponse("login.html", {"request": request})
    try:
        get_user_by_id_service(db, int(user_id))
    except ValueError as e:
        if str(e) == "User not found":
            return templates.TemplateResponse("login.html", {"request": request})
        else:
            return templates.TemplateResponse("dashboard.html", {"request": request, "error": str(e)})
    meal = MealCreate(
        user_id=user_id,
        date=date,
        time=time,
        type=type
    )
    try:
        create_meal_service(db, meal)
        response = RedirectResponse(url="/dashboard", status_code=303)
        response.set_cookie(key="user_id", value=str(user_id))
        return response
    except ValidationError as e:
        return templates.TemplateResponse("dashboard.html", {"request": request, "error": str(e)})