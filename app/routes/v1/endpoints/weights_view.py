from datetime import date, time
from pydantic_core._pydantic_core import ValidationError
from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.schemas import WeightCreate
from starlette.responses import RedirectResponse
from app.db.session import get_db
from app.services.weight_service import (
    get_weights_by_user_service, create_weight_service
)
from app.services.auth_service import get_current_web_active_user

router = APIRouter(
)

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def weights_view(
    request: Request, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_web_active_user)
):
    to_template = {
        "request": request,
    }
    to_template["username"] = current_user.username
    to_template["weights"] = get_weights_by_user_service(db, current_user.id)
    return templates.TemplateResponse("weights.html", to_template)

@router.post("/", response_class=HTMLResponse)
async def add_weight(
    request: Request,
    weight: float = Form(...),
    date: date = Form(...),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_web_active_user)
):
    weight = WeightCreate(
        weight=weight,
        user_id=current_user.id,
        date=date
    )
    try:
        create_weight_service(db, weight)
    except ValidationError as e:
        return templates.TemplateResponse("weights.html", {"request": request, "error": str(e)})
    return RedirectResponse("/weights_view", status_code=303)

