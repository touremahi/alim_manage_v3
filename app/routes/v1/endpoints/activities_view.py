from datetime import date, time, timedelta
from pydantic_core._pydantic_core import ValidationError
from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.schemas import ActivityCreate
from starlette.responses import RedirectResponse
from app.db.session import get_db
from app.services.activity_service import (
    get_activities_by_user_service, create_activity_service
)
from app.services.auth_service import get_current_web_active_user

router = APIRouter(
)

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def activities_view(
    request: Request, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_web_active_user)
):
    to_template = {
        "request": request,
    }
    to_template["username"] = current_user.username
    to_template["activities"] = get_activities_by_user_service(db, current_user.id)
    return templates.TemplateResponse("activities.html", to_template)

@router.post("/", response_class=HTMLResponse)
async def add_activity(
    request: Request,
    activity: str = Form(...),
    duration: int = Form(...),
    date: date = Form(...),
    time: time = Form(...),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_web_active_user)
):
    # duration.fromisoformat("00:00:00")
    activity = ActivityCreate(
        activity_type=activity,
        duration=timedelta(minutes=duration),
        date=date,
        time=time,
        user_id=current_user.id
    )
    try:
        create_activity_service(db, activity)
    except ValidationError as e:
        return templates.TemplateResponse("activities.html", {"request": request, "error": str(e)})
    return RedirectResponse("/activities_view", status_code=303)
