from sqlalchemy.orm import Session
from ..models import MealFood
from ..schemas import MealFoodCreate, MealFoodUpdate

# Create a new meal food, add food to meal
def create_meal_food(db: Session, meal_food: MealFoodCreate):
    db_meal_food = MealFood(
        meal_id = meal_food.meals.id,
        food_id = meal_food.foods.id,
        quantity = meal_food.quantity
    )
    db.add(db_meal_food)
    db.commit()
    db.refresh(db_meal_food)
    return db_meal_food

def get_meal_food_by_id(db: Session, meal_food_id: int):
    return db.query(MealFood).filter(MealFood.id == meal_food_id).first()

def get_meal_foods(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MealFood).offset(skip).limit(limit).all()

def get_meal_foods_by_meal_id(db: Session, meal_id: int):
    return db.query(MealFood).filter(MealFood.meal_id == meal_id).all()

def get_meal_foods_by_food_id(db: Session, food_id: int):
    return db.query(MealFood).filter(MealFood.food_id == food_id).all()

def update_meal_food(db: Session, meal_food_id: int, meal_food: MealFoodUpdate):
    db_meal_food = get_meal_food_by_id(db, meal_food_id)
    if db_meal_food is None:
        return None
    db_meal_food.meal_id = meal_food.meal_id
    db_meal_food.food_id = meal_food.food_id
    db_meal_food.quantity = meal_food.quantity

    db.commit()
    db.refresh(db_meal_food)
    return db_meal_food

def delete_meal_food(db: Session, meal_food_id: int):
    db_meal_food = get_meal_food_by_id(db, meal_food_id)
    if db_meal_food is None:
        return None
    db.delete(db_meal_food)
    db.commit()
    return db_meal_food