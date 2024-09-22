from pydantic_core._pydantic_core import ValidationError
from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.schemas.food import FoodCreate
from starlette.responses import RedirectResponse
from app.db.session import get_db
from app.services.food_service import (
    get_foods, create_food_service
)
from app.services.auth_service import get_current_web_active_user

router = APIRouter(
    dependencies=[Depends(get_current_web_active_user)]
)

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def foods_list(request: Request, db: Session = Depends(get_db)):
    foods = get_foods(db)

    return templates.TemplateResponse(
        "foods.html",
        {
            "request": request,
            "foods": foods
        }
    )

@router.post("/", response_class=HTMLResponse)
async def add_meal(
    request: Request,
    name: str = Form(...),
    category: str = Form(...),
    unit: str = Form(...),
    calories: float = Form(...),
    db: Session = Depends(get_db)
):
    food = FoodCreate(
        name=name,
        unit=unit,
        category=category,
        calories=calories
    )
    try:
        create_food_service(db, food)
        response = RedirectResponse(url="/foods_configs", status_code=303)
        return response
    except ValidationError as e:
        return templates.TemplateResponse("foods.html", {"request": request, "error": str(e)})
    