from app.schemas import MealFoodCreate, MealFoodUpdate
from app.repositories.meal_food_repository import (
    create_meal_food,
    get_meal_food_by_id,
    get_meal_foods,
    get_meal_foods_by_meal_id,
    get_meal_foods_by_food_id,
    update_meal_food,
    delete_meal_food,
)

# CRUD operations for MealFood model
def test_create_meal_food(db_session, meals, foods):
    meal_food_data = MealFoodCreate(
        meals=meals[-1],
        foods=foods[-1],
        quantity=100,
    )
    meal_food = create_meal_food(db_session, meal_food_data)
    assert meal_food.meals.id == meal_food_data.meals.id
    assert meal_food.foods.id == meal_food_data.foods.id
    assert meal_food.quantity == meal_food_data.quantity
    assert meal_food.id is not None

# get_meal_food_by_id
def test_get_meal_food_by_id(db_session, meal_foods):
    meal_food_id = meal_foods[-1].id
    meal_food = get_meal_food_by_id(db_session, meal_food_id)
    assert meal_food.meals.id == meal_foods[-1].meals.id
    assert meal_food.foods.id == meal_foods[-1].foods.id
    assert meal_food.quantity == meal_foods[-1].quantity
    assert meal_food.id == meal_foods[-1].id

# get_meal_foods
def test_get_meal_foods(db_session, meal_foods):
    meal_foods_list = get_meal_foods(db_session)
    assert len(meal_foods_list) == len(meal_foods)
    for meal_food in meal_foods_list:
        assert meal_food.id is not None
        assert meal_food.meals.id is not None
        assert meal_food.foods.id is not None
        assert meal_food.quantity is not None

# get_meal_foods_by_meal_id
def test_get_meal_foods_by_meal_id(db_session, meal_foods):
    meal_id = meal_foods[-1].meals.id
    meal_foods_list = get_meal_foods_by_meal_id(db_session, meal_id)
    for meal_food in meal_foods_list:
        assert meal_food.meals.id == meal_id
        assert meal_food.foods.id is not None
        assert meal_food.quantity is not None
        assert meal_food.id is not None

# get_meal_foods_by_food_id
def test_get_meal_foods_by_food_id(db_session, meal_foods):
    food_id = meal_foods[-1].foods.id
    meal_foods_list = get_meal_foods_by_food_id(db_session, food_id)
    for meal_food in meal_foods_list:
        assert meal_food.meals.id is not None
        assert meal_food.foods.id == food_id
        assert meal_food.quantity is not None
        assert meal_food.id is not None

# update_meal_food
def test_update_meal_food(db_session, meal_foods):
    meal_food_id = meal_foods[-1].id
    meal_food_data = MealFoodUpdate(
        meal_id=meal_foods[-1].meals.id,
        food_id=meal_foods[-1].foods.id,
        quantity=200
    )
    updated_meal_food = update_meal_food(db_session, meal_food_id, meal_food_data)
    assert updated_meal_food.quantity == meal_food_data.quantity
    assert updated_meal_food.id == meal_food_id
    assert updated_meal_food.meals.id == meal_food_data.meal_id
    assert updated_meal_food.foods.id == meal_food_data.food_id

# delete_meal_food
def test_delete_meal_food(db_session, meal_foods):
    meal_food_id = meal_foods[-1].id
    delete_meal_food(db_session, meal_food_id)
    deleted_meal_food = get_meal_food_by_id(db_session, meal_food_id)
    assert deleted_meal_food is None

