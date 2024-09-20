import datetime

from app.schemas import ActivityCreate
from app.repositories.activity_repository import (
    create_activity,
    get_activity_by_id,
    get_activities,
    get_activities_by_type,
    get_activities_by_date,
    get_activities_by_user,
    update_activity,
    delete_activity
)

# CRUD operations for Activity model
def test_create_activity(db_session, users):
    activity_data = ActivityCreate(
        user_id=users[-1].id,
        activity_type="Running",
        date=datetime.date(2023, 1, 1),
        time=datetime.time(10, 0, 0),
        duration=datetime.timedelta(seconds=3600)
    )
    activity = create_activity(db_session, activity_data)
    assert activity.user_id == users[-1].id
    assert activity.activity_type == "Running"
    assert activity.date == datetime.date(2023, 1, 1)
    assert activity.time == datetime.time(10, 0, 0)
    assert activity.duration == 3600
    assert activity.id is not None

# Get activities
def test_get_activities(db_session, activities):
    activities = get_activities(db_session)
    assert len(activities) == len(activities)
    for activity in activities:
        assert activity.id is not None
        assert activity.user_id is not None
        assert activity.activity_type is not None
        assert activity.date is not None
        assert activity.time is not None
        assert activity.duration is not None

# Get activity by ID
def test_get_activity_by_id(db_session, activities):
    activity = get_activity_by_id(db_session, activities[0].id)
    assert activity.id == activities[0].id
    assert activity.user_id == activities[0].user_id
    assert activity.activity_type == activities[0].activity_type
    assert activity.date == activities[0].date
    assert activity.time == activities[0].time
    assert activity.duration == activities[0].duration

# Get activity by type
def test_get_activities_by_type(db_session, activities):
    activity_type = activities[0].activity_type
    db_activities = get_activities_by_type(db_session, activity_type)
    for activity in db_activities:
        assert activity.activity_type == activity_type
        assert activity.date is not None
        assert activity.time is not None
        assert activity.duration is not None
        assert activity.id is not None
        assert activity.user_id is not None

# Get activity by date
def test_get_activities_by_date(db_session, activities):
    activity_date = activities[0].date
    db_activities = get_activities_by_date(db_session, activity_date)
    for activity in db_activities:
        assert activity.date == activity_date
        assert activity.time is not None
        assert activity.duration is not None
        assert activity.id is not None
        assert activity.user_id is not None
        assert activity.activity_type is not None

# Get activity by user
def test_get_activities_by_user(db_session, activities):
    user_id = activities[0].user_id
    db_activities = get_activities_by_user(db_session, user_id)
    for activity in db_activities:
        assert activity.user_id == user_id
        assert activity.activity_type is not None
        assert activity.date is not None
        assert activity.time is not None
        assert activity.duration is not None
        assert activity.id is not None

# Update activity
def test_update_activity(db_session, activities):
    activity_id = activities[0].id
    updated_activity_data = ActivityCreate(
        user_id=activities[0].user_id,
        activity_type="Swimming",
        date=datetime.date(2023, 1, 1),
        time=datetime.time(10, 0, 0),
        duration=datetime.timedelta(seconds=4000)
    )
    updated_activity = update_activity(db_session, activity_id, updated_activity_data)
    assert updated_activity.id == activity_id
    assert updated_activity.user_id == activities[0].user_id
    assert updated_activity.activity_type == "Swimming"
    assert updated_activity.date == datetime.date(2023, 1, 1)
    assert updated_activity.time == datetime.time(10, 0, 0)
    assert updated_activity.duration == 4000

# Delete activity
def test_delete_activity(db_session, activities):
    activity_id = activities[0].id
    delete_activity(db_session, activity_id)
    deleted_activity = get_activity_by_id(db_session, activity_id)
    assert deleted_activity is None


