from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....db.session import get_db
from ....schemas import WeightCreate, WeightOut
from ....services.weight_service import (
    create_weight_service, get_weights_service,
    get_weights_by_date_service, get_weights_by_user_service,
    get_weight_by_id_service, update_weight_service, 
    delete_weight_service
)

router = APIRouter()

@router.post("/", response_model=WeightOut)
def create_weight(weight: WeightCreate, db: Session = Depends(get_db)):
    return create_weight_service(db, weight)

@router.get("/", response_model=List[WeightOut])
def get_weights(db: Session = Depends(get_db)):
    try:
        return get_weights_service(db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{weight_id}", response_model=WeightOut)
def get_weight_by_id(weight_id: int, db: Session = Depends(get_db)):
    try:
        return get_weight_by_id_service(db, weight_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/user/{user_id}", response_model=List[WeightOut])
def get_weight_by_user_id(user_id: int, db: Session = Depends(get_db)):
    try:
        return get_weights_by_user_service(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/date/{date}", response_model=List[WeightOut])
def get_weight_by_date(date: str, db: Session = Depends(get_db)):
    try:
        return get_weights_by_date_service(db, date)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.put("/{weight_id}", response_model=WeightOut)
def update_weight(weight_id: int, weight: WeightCreate, db: Session = Depends(get_db)):
    try:
        return update_weight_service(db, weight_id, weight)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{weight_id}", response_model=WeightOut)
def delete_weight(weight_id: int, db: Session = Depends(get_db)):
    try:
        return delete_weight_service(db, weight_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

