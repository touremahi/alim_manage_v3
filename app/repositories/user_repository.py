from sqlalchemy.orm import Session
from ..models import User
from ..schemas import UserCreate, UserUpdate
from ..core.security import get_password_hash

# Create a new user
def create_user(db: Session, user: UserCreate):
    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=get_password_hash(user.password),
        age=user.age,
        initial_weight=user.initial_weight
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get a user by email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Get a user by id
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Get a user by username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Gets all users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

# Update a user
def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    if user.username:
        db_user.username = user.username
    if user.email:
        db_user.email = user.email
    if user.age:
        db_user.age = user.age
    if user.initial_weight:
        db_user.initial_weight = user.initial_weight

    db.commit()
    db.refresh(db_user)
    return db_user

# Delete a user
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
