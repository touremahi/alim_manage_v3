from app.schemas import MealFoodCreate, MealFoodUpdate
from app.services.meal_food_service import (
    add_food_to_meal_service,
    get_meal_food_by_id_service,
    get_meal_foods_by_meal_id_service,
    update_meal_food_service,
    delete_meal_food_service,
)

# Test add food to meal
def test_add_food_to_meal(db_session, meals, foods):
    meal_food_data = MealFoodUpdate(
        meal_id=meals[-1].id,
        food_id=foods[-1].id,
        quantity=100,
    )
    meal_food = add_food_to_meal_service(db_session, meal_food_data)
    assert meal_food.id is not None
    assert meal_food.meals.id == meal_food_data.meal_id
    assert meal_food.foods.id == meal_food_data.food_id
    assert meal_food.quantity == meal_food_data.quantity

# Test get meal food by id
def test_get_meal_food_by_id(db_session, meal_foods):
    meal_food_id = meal_foods[-1].id
    meal_food = get_meal_food_by_id_service(db_session, meal_food_id)
    assert meal_food.id == meal_food_id
    assert meal_food.meals.id == meal_foods[-1].meals.id
    assert meal_food.foods.id == meal_foods[-1].foods.id
    assert meal_food.quantity == meal_foods[-1].quantity

# Test get meal foods by meal id
def test_get_meal_foods_by_meal_id(db_session, meal_foods):
    meal_id = meal_foods[-1].meals.id
    meal_foods_list = get_meal_foods_by_meal_id_service(db_session, meal_id)
    assert len(meal_foods_list) >= 1
    for meal_food in meal_foods_list:
        assert meal_food.meals.id == meal_id
        assert meal_food.foods.id is not None
        assert meal_food.quantity is not None
        assert meal_food.id is not None

# Test update meal food
def test_update_meal_food(db_session, meal_foods):
    meal_food_id = meal_foods[-1].id
    meal_food = MealFoodUpdate(
        meal_id=meal_foods[-1].meals.id,
        food_id=meal_foods[-1].foods.id,
        quantity=100
    )
    updated_meal_food = update_meal_food_service(db_session, meal_food_id, meal_food)
    assert updated_meal_food.id == meal_food_id
    assert updated_meal_food.meals.id == meal_food.meal_id
    assert updated_meal_food.foods.id == meal_food.food_id
    assert updated_meal_food.quantity == meal_food.quantity
    assert updated_meal_food.id is not None

# Test delete meal food
def test_delete_meal_food(db_session, meal_foods):
    meal_food_id = meal_foods[-1].id
    delete_meal_food_service(db_session, meal_food_id)
    try:
        get_meal_food_by_id_service(db_session, meal_food_id)
    except Exception as e:
        assert str(e) == "Meal food not found"
