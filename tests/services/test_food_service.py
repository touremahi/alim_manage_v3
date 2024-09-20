from app.schemas import FoodCreate
from app.services.food_service import (
    create_food_service, get_food_by_id_service,
    get_foods_service, get_food_by_name_service,
    get_foods_by_category_service, update_food_service,
    delete_food_service
)

# Create a new food item
def test_create_food_service(db_session):
    food_data = FoodCreate(
        name="food1",
        unit="g",
        calories=10,
        category="Féculents"
    )
    food = create_food_service(db_session, food_data)
    assert food.name == food_data.name
    assert food.unit == food_data.unit
    assert food.calories == food_data.calories
    assert food.category == food_data.category
    assert food.id is not None

# get_food_by_id_service
def test_get_food_by_id_service(db_session, foods):
    food_id = foods[-1].id
    food = get_food_by_id_service(db_session, food_id)
    assert food.name == foods[-1].name
    assert food.unit == foods[-1].unit
    assert food.calories == foods[-1].calories
    assert food.category == foods[-1].category
    assert food.id == food_id

# get_foods_service
def test_get_foods_service(db_session, foods):
    foods_list = get_foods_service(db_session)
    assert len(foods_list) == len(foods)
    for food in foods_list:
        assert food.id is not None
        assert food.name is not None
        assert food.unit is not None
        assert food.calories is not None
        assert food.category is not None

# get_food_by_name_service
def test_get_food_by_name_service(db_session, foods):
    food_name = foods[-1].name
    food = get_food_by_name_service(db_session, food_name)
    assert food.name == food_name
    assert food.unit == foods[-1].unit
    assert food.calories == foods[-1].calories
    assert food.category == foods[-1].category
    assert food.id == foods[-1].id

# get_foods_by_category_service
def test_get_foods_by_category_service(db_session, foods):
    category = foods[-1].category
    foods_list = get_foods_by_category_service(db_session, category)
    assert len(foods_list) >= 1
    for food in foods_list:
        assert food.category == category
        assert food.id is not None
        assert food.name is not None
        assert food.unit is not None
        assert food.calories is not None

# update_food_service
def test_update_food_service(db_session, foods):
    food_id = foods[-1].id
    food_data = FoodCreate(
        name="food1",
        unit="g",
        calories=1.6,
        category="Féculents"
    )
    updated_food = update_food_service(db_session, food_id, food_data)
    assert updated_food.name == food_data.name
    assert updated_food.unit == food_data.unit
    assert updated_food.calories == food_data.calories
    assert updated_food.category == food_data.category
    assert updated_food.id == food_id

# delete_food_service
def test_delete_food_service(db_session, foods):
    food_id = foods[-1].id
    delete_food_service(db_session, food_id)
    try:
        get_food_by_id_service(db_session, food_id)
    except ValueError as e:
        assert str(e) == "Food not found"
    