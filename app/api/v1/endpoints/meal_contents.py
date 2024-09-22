from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....db.session import get_db
from ....schemas import MealContentOut
from ....services.meal_content_service import (
    get_meal_content_service
)
from app.services.auth_service import get_current_active_user

router = APIRouter(
    dependencies=[Depends(get_current_active_user)]
)

@router.get("/{meal_id}", response_model=MealContentOut)
def get_meal_content(meal_id: int, db: Session = Depends(get_db)):
    try:
        return get_meal_content_service(db, meal_id)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
