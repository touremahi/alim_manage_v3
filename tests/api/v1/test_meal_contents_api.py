
# Get the meal contents
def test_get_meal_content_service(client, meals, foods, meal_foods):
    meal_id = meals[-1].id
    response = client.get(f"/meal_contents/{meal_id}")
    assert response.status_code == 200
    assert response.json()["id"] == meal_id
    assert response.json()["user_id"] == meals[-1].user_id
    assert response.json()["date"] == str(meals[-1].date)
    assert response.json()["type"] == meals[-1].type
    assert response.json()["time"] == str(meals[-1].time)
    assert response.json()["foods"] is not None
