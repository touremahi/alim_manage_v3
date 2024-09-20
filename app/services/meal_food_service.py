from sqlalchemy.orm import Session
from ..schemas import MealFoodCreate, MealFoodOut, MealFoodUpdate
from ..repositories.meal_food_repository import (
    create_meal_food, get_meal_food_by_id, get_meal_foods_by_meal_id,
    update_meal_food, delete_meal_food
)

from .meal_service import get_meal_by_id_service
from .food_service import get_food_by_id_service

# Add a food to a meal
def add_food_to_meal_service(db: Session, meal_food: MealFoodUpdate):
    meal = get_meal_by_id_service(db, meal_food.meal_id)
    food = get_food_by_id_service(db, meal_food.food_id)
    if meal is None or food is None:
        raise ValueError("Meal or food not found")
    meal_food = MealFoodCreate(meals=meal, foods=food, quantity=meal_food.quantity)
    db_meal_food = create_meal_food(db, meal_food)
    return MealFoodOut(
        id=db_meal_food.id,
        meals=meal,
        foods=food,
        quantity=db_meal_food.quantity
    )

def get_meal_food_by_id_service(db: Session, meal_food_id: int):
    db_meal_food = get_meal_food_by_id(db, meal_food_id)
    if db_meal_food is None:
        raise ValueError("Meal food not found")
    meal_food = MealFoodOut(
        id=db_meal_food.id,
        meals=get_meal_by_id_service(db, db_meal_food.meal_id),
        foods=get_food_by_id_service(db, db_meal_food.food_id),
        quantity=db_meal_food.quantity
    )
    return meal_food

def get_meal_foods_by_meal_id_service(db: Session, meal_id: int):
    db_meal_foods = get_meal_foods_by_meal_id(db, meal_id)
    if not db_meal_foods:
        raise ValueError("No foods found for the given meal")
    meal_foods = [
        MealFoodOut(
            id=meal_food.id,
            meals=get_meal_by_id_service(db, meal_food.meal_id),
            foods=get_food_by_id_service(db, meal_food.food_id),
            quantity=meal_food.quantity
        )
        for meal_food in db_meal_foods
    ]
    return meal_foods

def update_meal_food_service(db: Session, meal_food_id: int, meal_food: MealFoodUpdate):
    meal = get_meal_by_id_service(db, meal_food.meal_id)
    food = get_food_by_id_service(db, meal_food.food_id)
    db_meal_food = get_meal_food_by_id_service(db, meal_food_id)
    if db_meal_food is None:
        raise ValueError("Meal food not found")
    updated_meal_food = update_meal_food(db, meal_food_id, meal_food)
    return MealFoodOut(
        id=updated_meal_food.id,
        meals=meal,
        foods=food,
        quantity=updated_meal_food.quantity
    )

def delete_meal_food_service(db: Session, meal_food_id: int):
    db_meal_food = get_meal_food_by_id_service(db, meal_food_id)
    if db_meal_food is None:
        raise ValueError("Meal food not found")
    delete_meal_food(db, meal_food_id)
    return db_meal_food