from datetime import datetime
from sqlalchemy.orm import Session
from ..schemas import WeightCreate, WeightOut
from ..repositories.weight_repository import (
    create_weight, get_weights, get_weight_by_id,
    get_weights_by_user_id, get_weights_by_date,
    update_weight, delete_weight
)

# Create a new weight
def create_weight_service(db: Session, weight: WeightCreate):
    db_weight = create_weight(db, weight)
    return WeightOut(**db_weight.__dict__)

# Get all weights
def get_weights_service(db: Session):
    db_weights = get_weights(db)
    if db_weights is None:
        raise ValueError("Weights not found")
    weights = [WeightOut(**weight.__dict__) for weight in db_weights]
    return weights

# Get a weight by id
def get_weight_by_id_service(db: Session, weight_id: int):
    db_weight = get_weight_by_id(db, weight_id)
    if db_weight is None:
        raise ValueError("Weight not found")
    return WeightOut(**db_weight.__dict__)

# Get a weight by user_id
def get_weights_by_user_service(db: Session, user_id: int):
    db_weights = get_weights_by_user_id(db, user_id)
    if db_weights is None:
        raise ValueError("Weight not found")
    weights = [WeightOut(**weight.__dict__) for weight in db_weights]
    return weights

# Get a weight by date
def get_weights_by_date_service(db: Session, date: str):
    db_weights = get_weights_by_date(db, date)
    if db_weights is None:
        raise ValueError("Weight not found")
    weights = [WeightOut(**weight.__dict__) for weight in db_weights]
    return weights

# Update a weight
def update_weight_service(db: Session, weight_id: int, weight: WeightCreate):
    db_weight = update_weight(db, weight_id, weight)
    if db_weight is None:
        raise ValueError("Weight not found")
    return WeightOut(**db_weight.__dict__)

# Delete a weight
def delete_weight_service(db: Session, weight_id: int):
    db_weight = delete_weight(db, weight_id)
    if db_weight is None:
        raise ValueError("Weight not found")
    return WeightOut(**db_weight.__dict__)
