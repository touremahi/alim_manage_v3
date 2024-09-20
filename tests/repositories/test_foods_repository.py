from app.schemas import FoodCreate
from app.repositories.food_repository import (
    create_food,
    get_food_by_id,
    get_food_by_name,
    get_foods,
    get_foods_by_category,
    update_food,
    delete_food,
)

# CRUD operations for Food model
def test_create_food(db_session):
    food_data = FoodCreate(
        name="food1",
        unit="g",
        calories=10,
        category="Féculents"
    )
    food = create_food(db_session, food_data)
    assert food.name == food_data.name
    assert food.unit == food_data.unit
    assert food.calories == food_data.calories
    assert food.category == food_data.category
    assert food.id is not None

# get_food_by_id
def test_get_food_by_id(db_session, foods):
    food_id = foods[-1].id
    food = get_food_by_id(db_session, food_id)
    assert food.name == foods[-1].name
    assert food.unit == foods[-1].unit
    assert food.calories == foods[-1].calories
    assert food.category == foods[-1].category
    assert food.id == food_id

# get_food_by_name
def test_get_food_by_name(db_session, foods):
    food_name = foods[-1].name
    food = get_food_by_name(db_session, food_name)
    assert food.name == food_name
    assert food.unit == foods[-1].unit
    assert food.calories == foods[-1].calories
    assert food.category == foods[-1].category
    assert food.id == foods[-1].id

# get_foods
def test_get_foods(db_session, foods):
    foods_list = get_foods(db_session)
    assert len(foods_list) == len(foods)
    for food in foods_list:
        assert food.id is not None
        assert food.name is not None
        assert food.unit is not None
        assert food.calories is not None
        assert food.category is not None

# get_foods_by_category
def test_get_foods_by_category(db_session, foods):
    category = foods[-1].category
    foods_list = get_foods_by_category(db_session, category)
    for food in foods_list:
        assert food.category == category

# update_food
def test_update_food(db_session, foods):
    food_id = foods[-1].id
    food_data = FoodCreate(
        name="food1",
        unit="g",
        calories=10,
        category="Féculents"
    )
    updated_food = update_food(db_session, food_id, food_data)
    assert updated_food.name == food_data.name
    assert updated_food.unit == food_data.unit
    assert updated_food.calories == food_data.calories
    assert updated_food.category == food_data.category
    assert updated_food.id == food_id

# delete_food
def test_delete_food(db_session, foods):
    food_id = foods[-1].id
    deleted_food = delete_food(db_session, food_id)
    assert deleted_food.id == food_id
    assert deleted_food.name == foods[-1].name
    assert deleted_food.unit == foods[-1].unit
    assert deleted_food.calories == foods[-1].calories
    assert deleted_food.category == foods[-1].category
    assert deleted_food.id == food_id
    assert delete_food(db_session, food_id) == None
