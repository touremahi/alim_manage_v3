from sqlalchemy.orm import Session
from ..schemas import UserCreate, UserUpdate, UserOut, UserInDB
from ..repositories.user_repository import (
    create_user, update_user, delete_user,
    get_user_by_email, get_user_by_id, get_users,
    get_user_by_username
)

# Create a new user
def create_user_service(db: Session, user: UserCreate):
    return create_user(db, user)

# get user by id
def get_user_by_id_service(db: Session, user_id: int):
    user_db = get_user_by_id(db, user_id)
    if not user_db:
        raise ValueError("User not found")
    user = UserOut(**user_db.__dict__)
    return user

# get user by email
def get_user_by_email_service(db: Session, email: str):
    user_db = get_user_by_email(db, email)
    if not user_db:
        raise ValueError("User not found")
    user = UserOut(**user_db.__dict__)
    return user

# Get all users
def get_users_service(db: Session):
    users_db = get_users(db)
    if not users_db:
        raise ValueError("No users found")
    users = [UserOut(**user.__dict__) for user in users_db]
    return users

def get_user_by_username_service(db: Session, username: str):
    user_db = get_user_by_username(db, username)
    if not user_db:
        raise ValueError("User not found")
    return UserInDB(**user_db.__dict__)

# get user in db
def get_user_in_db_service(db: Session, email: str):
    user_db = get_user_by_email(db, email)
    if not user_db:
        raise ValueError("User not found")
    return UserInDB(**user_db.__dict__)

# Update user information
def update_user_info(db: Session, user_id: int, user: UserUpdate):
    updated_user = update_user(db, user_id, user)
    if not updated_user:
        raise ValueError("User not found or update failed")
    return updated_user

# Delete a user
def delete_user_service(db: Session, user_id: int):
    deleted_user = delete_user(db, user_id)
    if not deleted_user:
        raise ValueError("User not found or deletion failed")
    return deleted_user
