from sqlalchemy.orm import Session
from ..models import Food
from ..schemas import FoodCreate

# Create a new food item
def create_food(db: Session, food: FoodCreate):
    db_food = Food(**food.__dict__)
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food

# Get a food item by ID
def get_food_by_id(db: Session, food_id: int):
    return db.query(Food).filter(Food.id == food_id).first()

# Get food by name
def get_food_by_name(db: Session, name: str):
    return db.query(Food).filter(Food.name == name).first()

# Get all food items
def get_foods(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Food).offset(skip).limit(limit).all()

# Get food by category
def get_foods_by_category(db: Session, category: str):
    return db.query(Food).filter(Food.category == category).all()

# Update food item
def update_food(db: Session, food_id: int, food: FoodCreate):
    db_food = db.query(Food).filter(Food.id == food_id).first()
    if db_food:
        for key, value in food.__dict__.items():
            setattr(db_food, key, value)
    db.commit()
    db.refresh(db_food)
    return db_food

# delete food item
def delete_food(db: Session, food_id: int):
    db_food = db.query(Food).filter(Food.id == food_id).first()
    if not db_food:
        return None
    db.delete(db_food)
    db.commit()
    return db_food
