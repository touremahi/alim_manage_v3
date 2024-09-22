from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....db.session import get_db
from ....schemas import MealCreate, MealOut
from ....services.meal_service import (
    create_meal_service, get_meals_service,
    get_meal_by_id_service, get_meals_by_user_service,
    get_meals_by_date_service,
    get_meals_by_type_service,
    get_meals_by_user_and_date_service, update_meal_service,
    delete_meal_service
)
from app.services.auth_service import get_current_active_user

router = APIRouter(
    dependencies=[Depends(get_current_active_user)]
)

@router.post("/", response_model=MealOut)
def create_meal(meal: MealCreate, db: Session = Depends(get_db)):
    try:
        return create_meal_service(db, meal)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.get("/", response_model=List[MealOut])
def get_meals(db: Session = Depends(get_db)):
    try:
        return get_meals_service(db)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.get("/{meal_id}", response_model=MealOut)
def get_meal_by_id(meal_id: int, db: Session = Depends(get_db)):
    try:
        return get_meal_by_id_service(db, meal_id)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.get("/date/{date}", response_model=List[MealOut])
def get_meals_by_date(date: str, db: Session = Depends(get_db)):
    try:
        return get_meals_by_date_service(db, date)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.get("/type/{meal_type}", response_model=List[MealOut])
def get_meals_by_type(meal_type: str, db: Session = Depends(get_db)):
    try:
        return get_meals_by_type_service(db, meal_type)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.get("/user/{user_id}", response_model=List[MealOut])
def get_meals_by_user(user_id: int, db: Session = Depends(get_db)):
    try:
        return get_meals_by_user_service(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    
@router.get("/user_date/{user_id}/{date}", response_model=List[MealOut])
def get_meals_by_user_date(user_id: int, date: str, db: Session = Depends(get_db)):
    try:
        return get_meals_by_user_and_date_service(db, user_id, date)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    
@router.put("/{meal_id}", response_model=MealOut)
def update_meal(meal_id: int, meal: MealCreate, db: Session = Depends(get_db)):
    try:
        return update_meal_service(db, meal_id, meal)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    
@router.delete("/{meal_id}", response_model=MealOut)
def delete_meal(meal_id: int, db: Session = Depends(get_db)):
    try:
        return delete_meal_service(db, meal_id)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))