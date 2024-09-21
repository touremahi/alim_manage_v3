from datetime import date
from sqlalchemy.orm import Session
from ..models import Meal
from ..schemas import MealCreate

# Create a new meal
def create_meal(db: Session, meal: MealCreate):
    db_meal = Meal(**meal.model_dump())
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal

# Get meals
def get_meals(db: Session):
    return db.query(Meal).all()

# Get a meal by ID
def get_meal_by_id(db: Session, meal_id: int):
    return db.query(Meal).filter(Meal.id == meal_id).first()

# get repas by date
def get_meals_by_date(db: Session, date: date):
    return db.query(Meal).filter(Meal.date == date).all()

# get repas by type
def get_meals_by_type(db: Session, type: str):
    return db.query(Meal).filter(Meal.type == type).all()

# get repas by user
def get_meals_by_user(db: Session, user_id: int):
    return db.query(Meal).filter(Meal.user_id == user_id).all()


# get meal by user and date
def get_meals_by_user_and_date(db: Session, user_id: int, date: date):
    return db.query(Meal).filter(Meal.user_id == user_id, Meal.date == date).all()

# Update a meal
def update_meal(db: Session, meal_id: int, meal: MealCreate):
    db_meal = get_meal_by_id(db, meal_id)
    if db_meal is None:
        return None
    for key, value in meal.__dict__.items():
        setattr(db_meal, key, value)
    db.commit()
    db.refresh(db_meal)
    return db_meal

# Delete a meal
def delete_meal(db: Session, meal_id: int):
    db_meal = get_meal_by_id(db, meal_id)
    if db_meal is None:
        return None
    db.delete(db_meal)
    db.commit()
    return db_meal