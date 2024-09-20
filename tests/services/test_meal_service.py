import datetime

from app.schemas import MealCreate
from app.services.meal_service import (
    create_meal_service, get_meal_by_id_service,
    get_meals_service, get_meals_by_type_service,
    get_meals_by_date_service, get_meals_by_user_and_date_service,
    get_meals_by_user_service, update_meal_service,
    delete_meal_service,
)

# Create a new meal
def test_create_meal_service(db_session, users):
    meal_data = MealCreate(
        user_id=users[-1].id,
        date=datetime.date(2023, 1, 1),
        type="meal1",
        time=datetime.time(12, 0)
    )
    meal = create_meal_service(db_session, meal_data)
    assert meal.user_id == meal_data.user_id
    assert meal.date == meal_data.date
    assert meal.type == meal_data.type
    assert meal.time == meal_data.time
    assert meal.id is not None

# get_meal_by_id_service
def test_get_meal_by_id_service(db_session, meals):
    meal_id = meals[-1].id
    meal = get_meal_by_id_service(db_session, meal_id)
    assert meal.user_id == meals[-1].user_id
    assert meal.date == meals[-1].date
    assert meal.type == meals[-1].type
    assert meal.time == meals[-1].time
    assert meal.id == meal_id

# get_meals_service
def test_get_meals_service(db_session, meals):
    meals_list = get_meals_service(db_session)
    assert len(meals_list) == len(meals)
    for meal in meals_list:
        assert meal.id is not None
        assert meal.user_id is not None
        assert meal.date is not None
        assert meal.type is not None
        assert meal.time is not None

# get_meals_by_type_service
def test_get_meals_by_type_service(db_session, meals):
    meal_type = meals[-1].type
    meals_list = get_meals_by_type_service(db_session, meal_type)
    assert len(meals_list) == 1
    for meal in meals_list:
        assert meal.type == meal_type
        assert meal.date is not None
        assert meal.time is not None
        assert meal.user_id is not None
        assert meal.id is not None

# get_meals_by_date_service
def test_get_meals_by_date_service(db_session, meals):
    date = meals[-1].date
    meals_list = get_meals_by_date_service(db_session, date)
    assert len(meals_list) == len(meals)   
    for meal in meals_list:
        assert meal.date == date
        assert meal.type is not None
        assert meal.time is not None
        assert meal.user_id is not None
        assert meal.id is not None

# get_meals_by_user_and_date_service
def test_get_meals_by_user_and_date_service(db_session, meals):
    user_id = meals[-1].user_id
    date = meals[-1].date
    meals_list = get_meals_by_user_and_date_service(db_session, user_id, date)
    assert len(meals_list) == 1
    for meal in meals_list:
        assert meal.user_id == user_id
        assert meal.date == date
        assert meal.type is not None
        assert meal.time is not None
        assert meal.id is not None

# get_meals_by_user_service
def test_get_meals_by_user_service(db_session, meals):
    user_id = meals[-1].user_id
    meals_list = get_meals_by_user_service(db_session, user_id)
    assert len(meals_list) == 1
    for meal in meals_list:
        assert meal.user_id == user_id
        assert meal.date is not None
        assert meal.type is not None
        assert meal.time is not None
        assert meal.id is not None

# update_meal_service
def test_update_meal_service(db_session, meals):
    meal_id = meals[-1].id
    meal_data = MealCreate(
        user_id=meals[-1].user_id,
        date=datetime.date(2023, 1, 2),
        type="meal25",
        time=datetime.time(13, 0)
    )
    updated_meal = update_meal_service(db_session, meal_id, meal_data)
    assert updated_meal.user_id == meal_data.user_id
    assert updated_meal.date == meal_data.date
    assert updated_meal.type == meal_data.type
    assert updated_meal.time == meal_data.time
    assert updated_meal.id == meal_id

# delete_meal_service
def test_delete_meal_service(db_session, meals):
    meal_id = meals[-1].id
    delete_meal_service(db_session, meal_id)
    try:
        get_meal_by_id_service(db_session, meal_id)
    except Exception as e:
        assert str(e) == "Meal not found"
