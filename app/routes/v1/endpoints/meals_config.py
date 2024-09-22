from pydantic_core._pydantic_core import ValidationError
from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.schemas.meal_food import MealFoodUpdate
from starlette.responses import RedirectResponse
from app.db.session import get_db
from app.services.user_service import get_users_service
from app.services.meal_service import get_meals_by_user_service
from app.services.food_service import get_foods_service
from app.services.meal_food_service import add_food_to_meal_service
from app.services.meal_content_service import (
    get_meal_content_service
)
from app.services.auth_service import get_current_web_active_user

router = APIRouter(
    dependencies=[Depends(get_current_web_active_user)]
)

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def meals_config(
    request: Request, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_web_active_user)
):
    to_template = {
        "request": request,
    }
    to_template["username"] = current_user.username
    to_template["meals"] = get_meals_by_user_service(db, current_user.id)
    to_template["foods"] = get_foods_service(db)
    to_template["users"] = get_users_service(db)
    return templates.TemplateResponse("meals.html", to_template)

@router.get("/{meal_id}", response_class=HTMLResponse)
async def meals_config(
    request: Request, meal_id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_web_active_user)
):
    to_template = {
        "request": request,
    }
    to_template["username"] = current_user.username
    to_template["meals"] = get_meals_by_user_service(db, current_user.id)
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
    meal = MealFoodUpdate(
        food_id=food,
        meal_id=meal,
        quantity=quantity
    )
    try:
        meal_food = add_food_to_meal_service(db, meal)
        response = RedirectResponse(url=f"/meals_configs/{meal_food.meals.id}", status_code=303)
        return response
    except ValidationError as e:
        return templates.TemplateResponse("meals.html", {"request": request, "error": str(e)})
