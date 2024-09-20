from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....db.session import get_db
from ....schemas import MealFoodOut, MealFoodUpdate
from ....services.meal_food_service import (
    add_food_to_meal_service, get_meal_food_by_id_service,
    get_meal_foods_by_meal_id_service,
    update_meal_food_service,
    delete_meal_food_service
)

router = APIRouter()

@router.post("/", response_model=MealFoodOut)
def add_food_to_meal(meal_food: MealFoodUpdate, db: Session = Depends(get_db)):
    try:
        return add_food_to_meal_service(db, meal_food)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.get("/{meal_food_id}", response_model=MealFoodOut)
def get_meal_food_by_id(meal_food_id: int, db: Session = Depends(get_db)):
    try:
        return get_meal_food_by_id_service(db, meal_food_id)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    
@router.get("/meal/{meal_id}", response_model=List[MealFoodOut])
def get_meal_foods_by_meal_id(meal_id: int, db: Session = Depends(get_db)):
    try:
        return get_meal_foods_by_meal_id_service(db, meal_id)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    
@router.put("/{meal_food_id}", response_model=MealFoodOut)
def update_meal_food(meal_food_id: int, meal_food: MealFoodUpdate, db: Session = Depends(get_db)):
    try:
        return update_meal_food_service(db, meal_food_id, meal_food)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    
@router.delete("/{meal_food_id}", response_model=MealFoodOut)
def delete_meal_food(meal_food_id: int, db: Session = Depends(get_db)):
    try:
        return delete_meal_food_service(db, meal_food_id)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))