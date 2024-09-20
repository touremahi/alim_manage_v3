from app.services.meal_content_service import (
    get_meal_content_service
)

# Test get meal content
def test_get_meal_content(db_session, meals, foods, meal_foods):
    meal_id = meals[-1].id
    meal_content = get_meal_content_service(db_session, meal_id)
    assert meal_content.id == meal_id
    assert meal_content.user_id == meals[-1].user_id
    assert meal_content.date == meals[-1].date
    assert meal_content.type == meals[-1].type
    assert meal_content.time == meals[-1].time
    assert meal_content.foods is not None
    