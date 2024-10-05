from datetime import date, time
from pydantic_core._pydantic_core import ValidationError
from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.schemas.meal_food import MealFoodCreate, MealFoodUpdate
from starlette.responses import RedirectResponse
from app.db.session import get_db
from app.services.user_service import (
    get_user_by_id_service, get_users_service
)
from app.services.meal_service import  get_meals_by_user_service
from app.services.food_service import  get_foods_service
from app.services.meal_food_service import (
    get_meal_foods_by_meal_id_service, add_food_to_meal_service
)
from app.services.meal_content_service import (
    get_meal_content_service
)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates/angular")

@router.get("/", response_class=HTMLResponse)
async def meals_config(request: Request, db: Session = Depends(get_db)):
    to_template = {
        "request": request,
    }
    user_id = request.cookies.get("user_id")
    if not user_id:
        return templates.TemplateResponse("login.html", {"request": request})
    to_template["username"] = get_user_by_id_service(db, int(user_id)).username
    to_template["meals"] = get_meals_by_user_service(db, user_id)
    to_template["foods"] = get_foods_service(db)
    to_template["users"] = get_users_service(db)
    return templates.TemplateResponse("meals.html", to_template)

@router.get("/{meal_id}", response_class=HTMLResponse)
async def meals_config(request: Request, meal_id: int, db: Session = Depends(get_db)):
    to_template = {
        "request": request,
    }
    user_id = request.cookies.get("user_id")
    if not user_id:
        return templates.TemplateResponse("login.html", {"request": request})
    to_template["username"] = get_user_by_id_service(db, int(user_id)).username
    to_template["meals"] = get_meals_by_user_service(db, user_id)
    to_template["foods"] = get_foods_service(db)
    to_template["meal_contents"] = get_meal_content_service(db, meal_id=meal_id)
    to_template["users"] = get_users_service(db)
    return templates.TemplateResponse("meals.html", to_template)

@router.post("/", response_class=HTMLResponse)
async def add_meal(
    request: Request,
    meal: int = Form(...),
    food: int = Form(...),
    quantity: float = Form(...),
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
            return templates.TemplateResponse("meals.html", {"request": request, "error": str(e)})
    meal = MealFoodUpdate(
        food_id=food,
        meal_id=meal,
        quantity=quantity
    )
    try:
        meal_food = add_food_to_meal_service(db, meal)
        response = RedirectResponse(url=f"/meals_configs/{meal_food.meals.id}", status_code=303)
        response.set_cookie(key="user_id", value=str(user_id))
        return response
    except ValidationError as e:
        return templates.TemplateResponse("meals.html", {"request": request, "error": str(e)})
