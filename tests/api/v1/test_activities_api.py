
# create activity test
def test_create_activity(client, users):
    user_id = users[0].id
    activity_data = {
        "activity_type": "test_activity",
        "duration": 3600,
        "date": "2024-09-18",
        "time": "14:00:00",
        "user_id": user_id
    }
    response = client.post("/activities/", json=activity_data)
    assert response.status_code == 200
    assert response.json()["activity_type"] == "test_activity"
    assert response.json()["duration"] == 3600
    assert response.json()["date"] == "2024-09-18"
    assert response.json()["time"] == "14:00:00"
    assert response.json()["user_id"] == user_id

# get activities test
def test_get_activities(client, activities):
    response = client.get("/activities/")
    assert response.status_code == 200
    assert len(response.json()) == len(activities)
    for activity in response.json():
        assert "id" in activity
        assert "activity_type" in activity
        assert "duration" in activity
        assert "date" in activity
        assert "time" in activity
        assert "user_id" in activity

# get activity by id test
def test_get_activity_by_id(client, activities):
    activity_id = activities[0].id
    response = client.get(f"/activities/{activity_id}")
    assert response.status_code == 200
    assert response.json()["activity_type"] == activities[0].activity_type
    assert response.json()["duration"] == activities[0].duration
    assert response.json()["date"] == str(activities[0].date)
    assert response.json()["time"] == str(activities[0].time)
    assert response.json()["user_id"] == activities[0].user_id
    assert response.json()["id"] == activity_id

# get activities by type test
def test_get_activities_by_type(client, activities):
    activity_type = activities[0].activity_type
    response = client.get(f"/activities/type/{activity_type}")
    assert response.status_code == 200
    assert len(response.json()) >= 1
    for activity in response.json():
        assert activity["activity_type"] == activity_type
        assert "id" in activity
        assert "duration" in activity
        assert "date" in activity
        assert "time" in activity
        assert "user_id" in activity
    
# get activities by user id test
def test_get_activities_by_user_id(client, activities):
    user_id = activities[0].user_id
    response = client.get(f"/activities/user/{user_id}")
    assert response.status_code == 200
    assert len(response.json()) >= 1
    for activity in response.json():
        assert activity["user_id"] == user_id
        assert "id" in activity
        assert "activity_type" in activity
        assert "duration" in activity
        assert "date" in activity
        assert "time" in activity

# update activity test
def test_update_activity(client, activities):
    activity_id = activities[0].id
    updated_activity_data = {
        "activity_type": "updated_activity",
        "duration": 7200,
        "date": "2024-09-19",
        "time": "15:00:00",
        "user_id": activities[0].user_id,
    }
    response = client.put(f"/activities/{activity_id}", json=updated_activity_data)
    assert response.status_code == 200
    assert response.json()["activity_type"] == "updated_activity"
    assert response.json()["duration"] == 7200
    assert response.json()["date"] == "2024-09-19"
    assert response.json()["time"] == "15:00:00"
    assert response.json()["user_id"] == activities[0].user_id
    assert response.json()["id"] == activity_id

# delete activity test
def test_delete_activity(client, activities):
    activity_id = activities[0].id
    response = client.delete(f"/activities/{activity_id}")
    assert response.status_code == 200

