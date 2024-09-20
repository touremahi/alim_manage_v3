from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....db.session import get_db
from ....schemas import FoodCreate, FoodOut
from ....services.food_service import (
    create_food_service,
    get_food_by_id_service, get_foods_service,
    get_foods_by_category_service, 
    update_food_service, delete_food_service
)

router = APIRouter()

@router.post("/", response_model=FoodOut)
def create_food(food: FoodCreate, db: Session = Depends(get_db)):
    return create_food_service(db, food)

@router.get("/", response_model=List[FoodOut])
def get_foods(db: Session = Depends(get_db)):
    return get_foods_service(db)

@router.get("/{food_id}", response_model=FoodOut)
def get_food_by_id(food_id: int, db: Session = Depends(get_db)):
    food = get_food_by_id_service(db, food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    return food

@router.get("/category/{category}", response_model=List[FoodOut])
def get_foods_by_category(category: str, db: Session = Depends(get_db)):
    return get_foods_by_category_service(db, category)

@router.put("/{food_id}", response_model=FoodOut)
def update_food(food_id: int, food: FoodCreate, db: Session = Depends(get_db)):
    return update_food_service(db, food_id, food)

@router.delete("/{food_id}", response_model=FoodOut)
def delete_food(food_id: int, db: Session = Depends(get_db)):
    try:
        return delete_food_service(db, food_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
