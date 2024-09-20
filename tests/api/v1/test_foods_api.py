
# Create a test for the create_food_service function
def test_create_food_service(client):
    # Create a FoodCreate object
    food_data = {
        "name": "Test Food",
        "unit": "Test Unit",
        "category": "Test Category",
        "calories": 100
    }
    response = client.post(
        "/foods/",
        json=food_data,
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Food"
    assert response.json()["unit"] == "Test Unit"
    assert response.json()["category"] == "Test Category"
    assert response.json()["calories"] == 100
    assert response.json()["id"] is not None

# Get all foods
def test_get_foods_service(client, foods):
    response = client.get("/foods/")
    assert response.status_code == 200
    assert len(response.json()) == len(foods)
    for food in response.json():
        assert "id" in food
        assert "name" in food
        assert "unit" in food
        assert "category" in food
        assert "calories" in food

# Get a food by id
def test_get_food_by_id_service(client, foods):
    food_id = foods[0].id
    response = client.get(f"/foods/{food_id}")
    assert response.status_code == 200
    assert response.json()["name"] == foods[0].name
    assert response.json()["unit"] == foods[0].unit
    assert response.json()["category"] == foods[0].category
    assert response.json()["calories"] == foods[0].calories
    assert response.json()["id"] == food_id

# Get foods by category
def test_get_foods_by_category_service(client, foods):
    category = foods[0].category
    response = client.get(f"/foods/category/{category}")
    assert response.status_code == 200
    for food in response.json():
        assert food["category"] == category
        assert "id" in food
        assert "name" in food
        assert "unit" in food
        assert "calories" in food

# Update a food
def test_update_food_service(client, foods):
    food_id = foods[0].id
    food_data = {
        "name": "Updated Food",
        "unit": "Updated Unit",
        "category": "Updated Category",
        "calories": 200
    }
    response = client.put(
        f"/foods/{food_id}",
        json=food_data,
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Food"
    assert response.json()["unit"] == "Updated Unit"
    assert response.json()["category"] == "Updated Category"
    assert response.json()["calories"] == 200
    assert response.json()["id"] == food_id

# Delete a food
def test_delete_food_service(client, foods):
    food_id = foods[0].id
    response = client.delete(f"/foods/{food_id}")
    assert response.status_code == 200

