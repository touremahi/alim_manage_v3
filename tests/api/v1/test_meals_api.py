
# create a meal
def test_create_meal(client, users):
    user_id = users[0].id
    meal_data = {
        "type": "Déjeuner",
        "date": "2024-09-18",
        "time": "12:00:00",
        "user_id": user_id
    }
    response = client.post(
        "/meals/",
        json=meal_data,
    )
    assert response.status_code == 200
    assert response.json()["type"] == "Déjeuner"
    assert response.json()["date"] == "2024-09-18"
    assert response.json()["time"] == "12:00:00"
    assert response.json()["user_id"] == user_id
    assert response.json()["id"] is not None

# get all meals
def test_get_meals(client, meals):
    response = client.get("/meals/")
    assert response.status_code == 200
    assert len(response.json()) == len(meals)
    for meal in response.json():
        assert "id" in meal
        assert "type" in meal
        assert "date" in meal
        assert "time" in meal
        assert "user_id" in meal

# get a meal by id
def test_get_meal(client, meals):
    meal_id = meals[0].id
    response = client.get(f"/meals/{meal_id}")
    assert response.status_code == 200
    assert response.json()["type"] == meals[0].type
    assert response.json()["date"] == str(meals[0].date)
    assert response.json()["time"] == str(meals[0].time)
    assert response.json()["user_id"] == meals[0].user_id
    assert response.json()["id"] == meal_id

# get meals by date
def test_get_meals_by_date(client, meals):
    date = meals[0].date
    response = client.get(f"/meals/date/{date}")
    assert response.status_code == 200
    assert len(response.json()) >= 1
    for meal in response.json():
        assert meal["date"] == str(date)
        assert meal["user_id"] is not None
        assert meal["id"] is not None
        assert meal["type"] is not None
        assert meal["time"] is not None
        assert meal["id"] is not None

# get meals by type
def test_get_meals_by_type(client, meals):
    meal_type = meals[0].type
    response = client.get(f"/meals/type/{meal_type}")
    assert response.status_code == 200
    assert len(response.json()) >= 1
    for meal in response.json():
        assert meal["type"] == meal_type
        assert meal["user_id"] is not None
        assert meal["id"] is not None
        assert meal["date"] is not None
        assert meal["time"] is not None

# get meals by user
def test_get_meals_by_user(client, meals):
    user_id = meals[0].user_id
    response = client.get(f"/meals/user/{user_id}")
    assert response.status_code == 200
    assert len(response.json()) >= 1
    for meal in response.json():
        assert meal["user_id"] == user_id
        assert meal["id"] is not None
        assert meal["date"] is not None
        assert meal["time"] is not None
        assert meal["type"] is not None

# get meals by user and date
def test_get_meals_by_user_and_date(client, meals):
    user_id = meals[0].user_id
    date = meals[0].date
    response = client.get(f"/meals/user_date/{user_id}/{date}")
    assert response.status_code == 200
    assert len(response.json()) >= 1
    for meal in response.json():
        assert meal["user_id"] == user_id
        assert meal["date"] == str(date)
        assert meal["id"] is not None
        assert meal["type"] is not None
        assert meal["time"]

# update meal info by id
def test_update_meal(client, meals):
    meal_id = meals[0].id
    user_id = meals[-1].user_id
    meal_data = {
        "type": "Déjeuner",
        "date": "2024-09-18",
        "time": "12:00:00",
        "user_id": user_id
    }
    response = client.put(
        f"/meals/{meal_id}",
        json=meal_data,
    )
    assert response.status_code == 200
    assert response.json()["type"] == "Déjeuner"
    assert response.json()["date"] == "2024-09-18"
    assert response.json()["time"] == "12:00:00"
    assert response.json()["user_id"] == user_id
    assert response.json()["id"] == meal_id

# delete a meal by id
def test_delete_meal(client, meals):
    meal_id = meals[0].id
    response = client.delete(f"/meals/{meal_id}")
    assert response.status_code == 200