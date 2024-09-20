import datetime

from app.schemas import ActivityCreate
from app.services.activity_service import (
    create_activity_service, get_activities_service,
    get_activity_by_id_service, get_activities_by_type_service,
    get_activities_by_date_service, get_activities_by_user_service,
    update_activity_service, delete_activity_service
)

# Test create activity
def test_create_activity(db_session, users):
    activity_data = ActivityCreate(
        user_id=users[-1].id,
        activity_type="Running",
        date=datetime.date(2024, 9, 20),
        time=datetime.time(10, 0, 0),
        duration=datetime.timedelta(seconds=3600)
    )
    activity = create_activity_service(db_session, activity_data)
    assert activity.user_id == users[-1].id
    assert activity.activity_type == "Running"
    assert activity.date == datetime.date(2024, 9, 20)
    assert activity.time == datetime.time(10, 0, 0)
    assert activity.duration == 3600
    assert activity.id is not None

# Test get activities
def test_get_activities(db_session, activities):
    activities = get_activities_service(db_session)
    assert len(activities) == len(activities)
    for activity in activities:
        assert activity.id is not None
        assert activity.user_id is not None
        assert activity.activity_type is not None
        assert activity.date is not None
        assert activity.time is not None
        assert activity.duration is not None

# Test get activity by ID
def test_get_activity_by_id(db_session, activities):
    activity_id = activities[0].id
    activity = get_activity_by_id_service(db_session, activity_id)
    assert activity.id == activity_id
    assert activity.user_id == activities[0].user_id
    assert activity.activity_type == activities[0].activity_type
    assert activity.date == activities[0].date
    assert activity.time == activities[0].time
    assert activity.duration == datetime.timedelta(seconds=activities[0].duration)

# Test get activities by type
def test_get_activities_by_type(db_session, activities):
    activity_type = activities[0].activity_type
    db_activities = get_activities_by_type_service(db_session, activity_type)
    for activity in db_activities:
        assert activity.activity_type == activity_type
        assert activity.user_id is not None
        assert activity.date is not None
        assert activity.time is not None
        assert activity.duration is not None
        assert activity.id is not None

# Test get activities by date
def test_get_activities_by_date(db_session, activities):
    date = activities[0].date
    db_activities = get_activities_by_date_service(db_session, date)
    for activity in db_activities:
        assert activity.date == date
        assert activity.user_id is not None
        assert activity.activity_type is not None
        assert activity.time is not None
        assert activity.duration is not None
        assert activity.id is not None

# Test get activities by user
def test_get_activities_by_user(db_session, activities):
    user_id = activities[0].user_id
    db_activities = get_activities_by_user_service(db_session, user_id)
    for activity in db_activities:
        assert activity.user_id == user_id
        assert activity.activity_type is not None
        assert activity.date is not None
        assert activity.time is not None
        assert activity.duration is not None
        assert activity.id is not None

# Test update activity
def test_update_activity(db_session, activities):
    activity_id = activities[0].id
    activity_data = ActivityCreate(
        user_id=activities[-1].user_id,
        activity_type="Swimming",
        date=datetime.date(2024, 9, 20),
        time=datetime.time(10, 0, 0),
        duration=datetime.timedelta(seconds=6200)
    )
    updated_activity = update_activity_service(db_session, activity_id, activity_data)
    assert updated_activity.id == activity_id
    assert updated_activity.user_id == activity_data.user_id
    assert updated_activity.activity_type == activity_data.activity_type
    assert updated_activity.date == activity_data.date
    assert updated_activity.time == activity_data.time
    assert updated_activity.duration == activity_data.duration
    assert updated_activity.id is not None

# Test delete activity
def test_delete_activity(db_session, activities):
    activity_id = activities[0].id
    delete_activity_service(db_session, activity_id)
    try:
        get_activity_by_id_service(db_session, activity_id)
    except Exception as e:
        assert str(e) == "Activity not found"
