from pydantic import BaseModel, ConfigDict
from datetime import date, time, timedelta
from typing import Optional

class ActivityBase(BaseModel):
    activity_type: str
    duration: timedelta
    date: date
    time: time

class ActivityCreate(ActivityBase):
    user_id: Optional[int] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "activity_type": "Marche",
                "duration": 3600,
                "date": "2024-09-18",
                "time": "14:00:00"
            }
        }
    }

class ActivityOut(ActivityBase):
    id: int
    user_id: int

    model_config = ConfigDict(
        ser_json_timedelta="float",
        from_attributes = True
    )
