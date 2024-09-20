from datetime import date
from sqlalchemy.orm import Session
from ..schemas import MealCreate, MealOut
from ..repositories.meal_repository import (
    create_meal, get_meal_by_id, get_meals_by_date, get_meals,
    get_meals_by_type, get_meals_by_user, update_meal,
    get_meals_by_user_and_date, delete_meal
)

# Create a new meal
def create_meal_service(db: Session, meal: MealCreate):
    db_meal = create_meal(db, meal)
    return MealOut(**db_meal.__dict__)

# Get meal by ID
def get_meal_by_id_service(db: Session, meal_id: int):
    meal_db = get_meal_by_id(db, meal_id)
    if meal_db is None:
        raise ValueError("Meal not found")
    meal = MealOut(**meal_db.__dict__)
    return meal

# Get meals
def get_meals_service(db: Session):
    db_meals = get_meals(db)
    if db_meals is None:
        raise ValueError("No meals found")
    meals = [MealOut(**meal.__dict__) for meal in db_meals]
    return meals

# Get meals by type
def get_meals_by_type_service(db: Session, meal_type: str):
    db_meals = get_meals_by_type(db, meal_type)
    if db_meals is None:
        raise ValueError("No meals found for the given type")
    meals = [MealOut(**meal.__dict__) for meal in db_meals]
    return meals

# Get meals by date
def get_meals_by_date_service(db: Session, date: date):
    db_meals = get_meals_by_date(db, date)
    if db_meals is None:
        raise ValueError("No meals found for the given date")
    meals = [MealOut(**meal.__dict__) for meal in db_meals]
    return meals

# get meal by user and date
def get_meals_by_user_and_date_service(db: Session, user_id: int, date: date):
    db_meals = get_meals_by_user_and_date(db, user_id, date)
    if db_meals is None:
        raise ValueError("No meals found for the given date")
    meals = [MealOut(**meal.__dict__) for meal in db_meals]
    return meals

# get meal by user
def get_meals_by_user_service(db: Session, user_id: int):
    db_meals = get_meals_by_user(db, user_id)
    if db_meals is None:
        raise ValueError("No meals found for the given user")
    meals = [MealOut(**meal.__dict__) for meal in db_meals]
    return meals
    
# update meal
def update_meal_service(db: Session, meal_id: int, meal: MealCreate):
    updated_meal = update_meal(db, meal_id, meal)
    if not updated_meal:
        raise ValueError("Meal not found or update failed")
    return MealOut(**updated_meal.__dict__)

# delete meal
def delete_meal_service(db: Session, meal_id: int):
    deleted_meal = delete_meal(db, meal_id)
    if deleted_meal is None:
        raise ValueError("Meal not found or deletion failed")
    return MealOut(**deleted_meal.__dict__)
