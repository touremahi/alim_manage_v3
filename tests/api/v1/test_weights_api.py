
# Create a new weight entry
def test_create_weight(client, users):
    user_id = users[0].id
    weight_data = {
        "date": "2024-09-18",
        "weight": 82,
        "user_id": user_id
    }
    response = client.post(
        "/weights/",
        json=weight_data,
    )
    assert response.status_code == 200
    assert response.json()["weight"] == 82
    assert response.json()["date"] == "2024-09-18"
    assert response.json()["user_id"] == user_id
    assert response.json()["id"] is not None

# get all weights
def test_get_weights(client, weights):
    response = client.get("/weights/")
    assert response.status_code == 200
    assert len(response.json()) == len(weights)
    for weight in response.json():
        assert "id" in weight
        assert "weight" in weight
        assert "date" in weight
        assert "user_id" in weight

# get a weight by id
def test_get_weight(client, weights):
    weight_id = weights[0].id
    response = client.get(f"/weights/{weight_id}")
    assert response.status_code == 200
    assert response.json()["weight"] == weights[0].weight
    assert response.json()["date"] == str(weights[0].date)
    assert response.json()["user_id"] == weights[0].user_id
    assert response.json()["id"] == weight_id

# get weights by user id
def test_get_weights_by_user_id(client, weights):
    user_id = weights[0].user_id
    response = client.get(f"/weights/user/{user_id}")
    assert response.status_code == 200
    assert len(response.json()) >= 1
    for weight in response.json():
        assert "id" in weight
        assert "weight" in weight
        assert "date" in weight
        assert weight["user_id"] == user_id

# get weights by date
def test_get_weights_by_date(client, weights):
    date = weights[0].date
    response = client.get(f"/weights/date/{date}")
    assert response.status_code == 200
    assert len(response.json()) >= 1
    for weight in response.json():
        assert "id" in weight
        assert "weight" in weight
        assert weight["date"] == str(date)
        assert "user_id" in weight

# update weight
def test_update_weight(client, weights):
    weight_id = weights[0].id
    weight_data = {
        "weight": 85,
        "date": "2024-09-19",
        "user_id": weights[0].user_id
    }
    response = client.put(
        f"/weights/{weight_id}",
        json=weight_data,
    )
    assert response.status_code == 200
    assert response.json()["weight"] == 85
    assert response.json()["date"] == "2024-09-19"
    assert response.json()["user_id"] == weights[0].user_id
    assert response.json()["id"] == weight_id

# delete weight
def test_delete_weight(client, weights):
    weight_id = weights[0].id
    response = client.delete(f"/weights/{weight_id}")
    assert response.status_code == 200
