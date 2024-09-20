from sqlalchemy.orm import Session
from ..schemas import MealContentOut, MealFoodOutCalories
from ..repositories.meal_repository import get_meal_by_id
from ..repositories.meal_food_repository import get_meal_foods_by_meal_id

def get_meal_content_service(db: Session, meal_id: int):
    db_meal = get_meal_by_id(db, meal_id)
    if db_meal is None:
        raise ValueError("Meal not found")
    db_meal_foods = get_meal_foods_by_meal_id(db, meal_id)
    meal_foods = []
    for meal_food in db_meal_foods:
        meal_food_out = MealFoodOutCalories(
            id = meal_food.id,
            name = meal_food.foods.name,
            category = meal_food.foods.category,
            quantity = meal_food.quantity,
            calories = meal_food.foods.calories * meal_food.quantity
        )
        meal_foods.append(meal_food_out)

    meal_content = MealContentOut(
        **db_meal.__dict__,
        foods=meal_foods
    )
    return meal_content
    



