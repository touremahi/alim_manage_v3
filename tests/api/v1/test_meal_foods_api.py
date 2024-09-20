
# add food to meal
def test_add_food_to_meal(client, meals, foods):
    meal_id = meals[0].id
    food_id = foods[0].id
    meal_food_data = {
        "meal_id" : meal_id,
        "food_id" : food_id,
        "quantity" : 100
    }
    response = client.post(
        f"/meal_foods/",
        json=meal_food_data,
    )
    assert response.status_code == 200
    assert response.json()["meals"]["id"] == meal_id
    assert response.json()["foods"]["id"] == food_id
    assert response.json()["quantity"] == 100
    assert response.json()["id"] is not None

# get meal_foods by id
def test_get_meal_food(client, meal_foods):
    meal_food_id = meal_foods[0].id
    meal_id = meal_foods[0].meals.id
    food_id = meal_foods[0].foods.id
    quantity = meal_foods[0].quantity
    response = client.get(f"/meal_foods/{meal_food_id}")
    assert response.status_code == 200
    assert response.json()["id"] == meal_food_id
    assert response.json()["meals"]["id"] == meal_id
    assert response.json()["foods"]["id"] == food_id
    assert response.json()["quantity"] == quantity

# get meal_foods by meal id
def test_get_meal_foods_by_meal_id(client, meal_foods):
    meal_id = meal_foods[0].meals.id
    response = client.get(f"/meal_foods/meal/{meal_id}")
    assert response.status_code == 200
    assert len(response.json()) >= 1
    for meal_food in response.json():
        assert meal_food["meals"]["id"] == meal_id
        assert "foods" in meal_food
        assert "quantity" in meal_food
        assert "id" in meal_food

# update meal_food
def test_update_meal_food(client, meal_foods, meals, foods):
    meal_food_id = meal_foods[0].id
    new_meal_food_data = {
        "meal_id" : meals[-1].id,
        "food_id" : foods[-1].id,
        "quantity" : 200
    }
    response = client.put(
        f"/meal_foods/{meal_food_id}",
        json=new_meal_food_data,
    )
    assert response.status_code == 200
    assert response.json()["id"] == meal_food_id
    assert response.json()["meals"]["id"] == new_meal_food_data["meal_id"]
    assert response.json()["foods"]["id"] == new_meal_food_data["food_id"]
    assert response.json()["quantity"] == new_meal_food_data["quantity"]

# delete meal_food
def test_delete_meal_food(client, meal_foods):
    meal_food_id = meal_foods[0].id
    response = client.delete(f"/meal_foods/{meal_food_id}")
    assert response.status_code == 200
