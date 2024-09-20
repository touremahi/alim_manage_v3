from sqlalchemy.orm import Session
from ..schemas import FoodCreate, FoodOut
from ..repositories.food_repository import (
    create_food, get_food_by_id, get_foods,
    get_foods_by_category, get_food_by_name,
    update_food, delete_food
)

# Create a new food item
def create_food_service(db: Session, food: FoodCreate):
    db_food = create_food(db, food)
    return FoodOut(**db_food.__dict__)

# Get all food items
def get_foods_service(db: Session):
    db_foods = get_foods(db)
    if db_foods is None:
        raise ValueError("Food not found")
    foods = [FoodOut(**food.__dict__) for food in db_foods]
    return foods

# Get food by name
def get_food_by_name_service(db: Session, name: str):
    db_food = get_food_by_name(db, name)
    if db_food is None:
        raise ValueError("Food not found")
    return FoodOut(**db_food.__dict__)

# get food by id
def get_food_by_id_service(db: Session, food_id: int):
    food = get_food_by_id(db, food_id)
    if food is None:
        raise ValueError("Food not found")
    return FoodOut(**food.__dict__)

# get food by category
def get_foods_by_category_service(db: Session, category: str):
    db_foods = get_foods_by_category(db, category)
    if db_foods is None:
        raise ValueError("Food not found")
    foods = [FoodOut(**food.__dict__) for food in db_foods]
    return foods

# Update food item
def update_food_service(db: Session, food_id: int, food: FoodCreate):
    updated_food = update_food(db, food_id, food)
    if updated_food is None:
        raise ValueError("Food not found")
    return FoodOut(**updated_food.__dict__)

# delete food item
def delete_food_service(db: Session, food_id: int):
    deleted_food = delete_food(db, food_id)
    if deleted_food is None:
        raise ValueError("Food not found or deletion failed")
    return FoodOut(**deleted_food.__dict__)
