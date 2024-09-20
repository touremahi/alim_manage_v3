
# Create a new user
def test_create_user(client):
    user_data = {
        "age": 30,
        "email": "johndoe@example.com",
        "initial_weight": 70.5,
        "password": "password123",
        "username": "John Doe"
    }
    response = client.post(
        "/users/",
        json=user_data,
    )
    assert response.status_code == 200
    assert response.json()["username"] == "John Doe"
    assert response.json()["email"] == "johndoe@example.com"
    assert response.json()["age"] == 30
    assert response.json()["initial_weight"] == 70.5
    assert response.json()["id"] is not None

# get all users
def test_get_users(client, users):
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) == len(users)
    for user in response.json():
        assert "id" in user
        assert "username" in user
        assert "email" in user
        assert "age" in user
        assert "initial_weight" in user

# get a user by id
def test_get_user(client, users):
    user_id = users[0].id
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["username"] == users[0].username
    assert response.json()["email"] == users[0].email
    assert response.json()["age"] == users[0].age
    assert response.json()["initial_weight"] == users[0].initial_weight
    assert response.json()["id"] == user_id

# get user by email
def test_get_user_by_email(client, users):
    user_email = users[0].email
    response = client.get(f"/users/email/{user_email}")
    assert response.status_code == 200
    assert response.json()["username"] == users[0].username
    assert response.json()["email"] == user_email
    assert response.json()["age"] == users[0].age
    assert response.json()["initial_weight"] == users[0].initial_weight
    assert response.json()["id"] == users[0].id

# update user info by id
def test_update_user(client, users):
    user_id = users[0].id
    updated_user_data = {
        "age": 31,
        "username": "John Doe Updated",
        "email": "johndoe@example.com",
        "initial_weight": 71.5
    }
    response = client.put(
        f"/users/{user_id}",
        json=updated_user_data,
    )
    assert response.status_code == 200
    assert response.json()["username"] == updated_user_data["username"]
    assert response.json()["email"] == updated_user_data["email"]
    assert response.json()["age"] == updated_user_data["age"]
    assert response.json()["initial_weight"] == updated_user_data["initial_weight"]
    assert response.json()["id"] == user_id

# delete user by id
def test_delete_user(client, users):
    user_id = users[0].id
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
