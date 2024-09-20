from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....db.session import get_db
from ....schemas.user import UserCreate, UserOut, UserUpdate, UserInDB
from ....services.user_service import (
    create_user_service, update_user_info, delete_user_service,
    get_user_by_id_service, get_user_by_email_service, get_users_service
)

router = APIRouter()

# Create a new user
@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(db, user)

# Get list of users
@router.get("/", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    try:
        users = get_users_service(db)
        return users
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = get_user_by_id_service(db, user_id)
        return user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# Get user by email
@router.get("/email/{email}", response_model=UserOut)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    try:
        user = get_user_by_email_service(db, email)
        return user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# Update user info by id
@router.put("/{user_id}", response_model=UserOut)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    
    try:
        updated_user = update_user_info(db, user_id, user)
        return updated_user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# Delete user by id
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        deleted_user = delete_user_service(db, user_id)
        return deleted_user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
