from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class WeightBase(BaseModel):
    weight: float
    date: date

class WeightCreate(WeightBase):
    user_id: Optional[int] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "weight": 82,
                "date": "2024-09-18",
                "user_id": 1
            }
        }
    }

class WeightOut(WeightBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes = True)