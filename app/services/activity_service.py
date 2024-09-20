from sqlalchemy.orm import Session
from ..schemas import ActivityCreate, ActivityOut
from ..repositories.activity_repository import (
    create_activity, update_activity, delete_activity,
    get_activities, get_activity_by_id, get_activities_by_type,
    get_activities_by_date, get_activities_by_user
)

# Create a new activity
def create_activity_service(db: Session, activity: ActivityCreate):
    return create_activity(db, activity)

# get activities
def get_activities_service(db: Session):
    db_activities = get_activities(db)
    if db_activities is None:
        raise ValueError("No activities found")
    activities = [ActivityOut(**activity.__dict__) for activity in db_activities]
    return activities

# get activity by id
def get_activity_by_id_service(db: Session, activity_id: int):
    db_activity = get_activity_by_id(db, activity_id)
    if db_activity is None:
        raise ValueError("Activity not found")
    return ActivityOut(**db_activity.__dict__)

# get activities by type
def get_activities_by_type_service(db: Session, activity_type: str):
    db_activities = get_activities_by_type(db, activity_type)
    if db_activities is None:
        raise ValueError("Activity not found")
    activities = [ActivityOut(**activity.__dict__) for activity in db_activities]
    return activities

# get activities by date
def get_activities_by_date_service(db: Session, activity_date: str):
    db_activities = get_activities_by_date(db, activity_date)
    if db_activities is None:
        raise ValueError("Activity not found")
    activities = [ActivityOut(**activity.__dict__) for activity in db_activities]
    return activities

# get activities by user
def get_activities_by_user_service(db: Session, user_id: int):
    db_activities = get_activities_by_user(db, user_id)
    if db_activities is None:
        raise ValueError("Activity not found")
    activities = [ActivityOut(**activity.__dict__) for activity in db_activities]
    return activities

# update activity
def update_activity_service(db: Session, activity_id: int, activity: ActivityCreate):
    updated_activity = update_activity(db, activity_id, activity)
    if updated_activity is None:
        raise ValueError("Activity not found")
    return ActivityOut(**updated_activity.__dict__)

# delete activity
def delete_activity_service(db: Session, activity_id: int):
    deleted_activity = delete_activity(db, activity_id)
    if deleted_activity is None:
        raise ValueError("Activity not found")
    return ActivityOut(**deleted_activity.__dict__)