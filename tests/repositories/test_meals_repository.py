import datetime

from app.schemas import MealCreate
from app.repositories.meal_repository import (
    create_meal,
    get_meal_by_id,
    get_meals,
    get_meals_by_user,
    get_meals_by_date,
    get_meals_by_type,
    get_meals_by_user_and_date,
    update_meal,
    delete_meal,
)

# CRUD operations for Meal model
def test_create_meal(db_session, users):
    meal_data = MealCreate(
        user_id=users[-1].id,
        date=datetime.date(2023, 1, 1),
        type="meal1",
        time=datetime.time(12, 0)
    )
    meal = create_meal(db_session, meal_data)
    assert meal.user_id == meal_data.user_id
    assert meal.date == meal_data.date
    assert meal.type == meal_data.type
    assert meal.time == meal_data.time
    assert meal.id is not None

# get_meal_by_id
def test_get_meal_by_id(db_session, meals):
    meal_id = meals[-1].id
    meal = get_meal_by_id(db_session, meal_id)
    assert meal.user_id == meals[-1].user_id
    assert meal.date == meals[-1].date
    assert meal.type == meals[-1].type
    assert meal.time == meals[-1].time
    assert meal.id == meals[-1].id

# get_meals
def test_get_meals(db_session, meals):
    meals_list = get_meals(db_session)
    assert len(meals_list) == len(meals)
    for meal in meals_list:
        assert meal.id is not None
        assert meal.user_id is not None
        assert meal.date is not None
        assert meal.type is not None
        assert meal.time is not None

# get mealls by user
def test_get_meals_by_user(db_session, meals):
    user_id = meals[-1].user_id
    meals_list = get_meals_by_user(db_session, user_id)
    assert len(meals_list) == 1
    for meal in meals_list:
        assert meal.user_id == user_id
        assert meal.date is not None
        assert meal.type is not None
        assert meal.time is not None

# get meals by date
def test_get_meals_by_date(db_session, meals):
    date = meals[-1].date
    meals_list = get_meals_by_date(db_session, date)
    for meal in meals_list:
        assert meal.date == date

# get meals by type
def test_get_meals_by_type(db_session, meals):
    type = meals[-1].type
    meals_list = get_meals_by_type(db_session, type)
    assert len(meals_list) == 1
    for meal in meals_list:
        assert meal.type == type
        assert meal.date is not None
        assert meal.time is not None
        assert meal.user_id is not None
        assert meal.id is not None

# get meals by user and date
def test_get_meals_by_user_and_date(db_session, meals):
    user_id = meals[-1].user_id
    date = meals[-1].date
    meals_list = get_meals_by_user_and_date(db_session, user_id, date)
    assert len(meals_list) == 1
    for meal in meals_list:
        assert meal.user_id == user_id
        assert meal.date == date
        assert meal.type is not None
        assert meal.time is not None
        assert meal.id is not None

# update meal
def test_update_meal(db_session, meals):
    meal_id = meals[-1].id
    meal_data = MealCreate(
        user_id=meals[-1].user_id,
        date=datetime.date(2023, 1, 2),
        type="meal55",
        time=datetime.time(12, 0)
    )
    updated_meal = update_meal(db_session, meal_id, meal_data)
    assert updated_meal.user_id == meal_data.user_id
    assert updated_meal.date == meal_data.date
    assert updated_meal.type == meal_data.type
    assert updated_meal.time == meal_data.time
    assert updated_meal.id == meal_id

# delete meal
def test_delete_meal(db_session, meals):
    meal_id = meals[-1].id
    delete_meal(db_session, meal_id)
    deleted_meal = get_meal_by_id(db_session, meal_id)
    assert deleted_meal is None
