from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....db.session import get_db
from ....schemas import ActivityCreate, ActivityOut
from ....services.activity_service import (
    create_activity_service, get_activities_service,
    get_activity_by_id_service, get_activities_by_type_service,
    get_activities_by_user_service,
    update_activity_service, delete_activity_service
)

router = APIRouter()

@router.post("/", response_model=ActivityOut)
def create_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    return create_activity_service(db, activity)

@router.get("/", response_model=List[ActivityOut])
def get_activities(db: Session = Depends(get_db)):
    try:
        return get_activities_service(db)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    
@router.get("/{activity_id}", response_model=ActivityOut)
def get_activity_by_id(activity_id: int, db: Session = Depends(get_db)):
    try:
        return get_activity_by_id_service(db, activity_id)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    
@router.get("/type/{activity_type}", response_model=List[ActivityOut])
def get_activities_by_type(activity_type: str, db: Session = Depends(get_db)):
    try:
        return get_activities_by_type_service(db, activity_type)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.get("/user/{user_id}", response_model=List[ActivityOut])
def get_activity_by_user(user_id: int, db: Session = Depends(get_db)):
    try:
        return get_activities_by_user_service(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.put("/{activity_id}", response_model=ActivityOut)
def update_activity(activity_id: int, activity: ActivityCreate, db: Session = Depends(get_db)):
    try:
        return update_activity_service(db, activity_id, activity)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    
@router.delete("/{activity_id}", response_model=ActivityOut)
def delete_activity(activity_id: int, db: Session = Depends(get_db)):
    try:
        return delete_activity_service(db, activity_id)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
