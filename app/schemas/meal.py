from pydantic import BaseModel, ConfigDict
from datetime import date, time

class MealBase(BaseModel):
    type: str
    date: date
    time: time
    user_id: int

class MealCreate(MealBase):

    model_config = {
        "json_schema_extra": {
            "example": {
                "type": "Déjeuner",
                "date": "2024-09-18",
                "time": "12:00:00",
                "user_id": 1
            }
        }
    }

class MealOut(MealBase):
    id: int

    model_config = ConfigDict(from_attributes = True)
