from sqlalchemy.orm import Session
from ..models import Weight
from ..schemas import WeightCreate

# Create a new weight
def create_weight(db: Session, weight: WeightCreate):
    db_weight = Weight(**weight.model_dump())
    db.add(db_weight)
    db.commit()
    db.refresh(db_weight)
    return db_weight

# Get all weights
def get_weights(db: Session):
    return db.query(Weight).all()

# Get a weight by id
def get_weight_by_id(db: Session, weight_id: int):
    return db.query(Weight).filter(Weight.id == weight_id).first()

# get a weight by user_id
def get_weights_by_user_id(db: Session, user_id: int):
    return db.query(Weight).filter(Weight.user_id == user_id).all()

# get a weight by date
def get_weights_by_date(db: Session, date: str):
    return db.query(Weight).filter(Weight.date == date).all()

# update a weight
def update_weight(db: Session, weight_id: int, weight: WeightCreate):
    db_weight = get_weight_by_id(db, weight_id)
    if db_weight is None:
        return None
    for key, value in weight.model_dump().items():
        setattr(db_weight, key, value)
    db.commit()
    db.refresh(db_weight)
    return db_weight

# delete a weight
def delete_weight(db: Session, weight_id: int):
    db_weight = get_weight_by_id(db, weight_id)
    if db_weight is None:
        return None
    db.delete(db_weight)
    db.commit()
    return db_weight

