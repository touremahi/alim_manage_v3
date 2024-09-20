from sqlalchemy.orm import Session
from ..models import Activity
from ..schemas import ActivityCreate

# Create a new activity
def create_activity(db: Session, activity: ActivityCreate):
    db_activity = Activity(**activity.__dict__)
    db_activity.duration = activity.duration.total_seconds()
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

# Get activities
def get_activities(db: Session):
    return db.query(Activity).all()

# Get activity by ID
def get_activity_by_id(db: Session, activity_id: int):
    return db.query(Activity).filter(Activity.id == activity_id).first()

# Get activity by type
def get_activities_by_type(db: Session, activity_type: str):
    return db.query(Activity).filter(Activity.activity_type == activity_type).all()

# Get activity by date
def get_activities_by_date(db: Session, activity_date: str):
    return db.query(Activity).filter(Activity.date == activity_date).all()

# Get activity by user
def get_activities_by_user(db: Session, user_id: int):
    return db.query(Activity).filter(Activity.user_id == user_id).all()

# Updatee activity
def update_activity(db: Session, activity_id: int, activity: ActivityCreate):
    db_activity = db.query(Activity).filter(Activity.id == activity_id).first()
    if db_activity is None:
        return None
    for key, value in activity.__dict__.items():
        if key == 'duration':
            setattr(db_activity, key, value.total_seconds())
            continue
        setattr(db_activity, key, value)
    db.commit()
    db.refresh(db_activity)
    return db_activity

# Delete activity
def delete_activity(db: Session, activity_id: int):
    db_activity = db.query(Activity).filter(Activity.id == activity_id).first()
    if db_activity is None:
        return None
    db.delete(db_activity)
    db.commit()
    return db_activity