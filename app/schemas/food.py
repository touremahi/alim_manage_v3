from pydantic import BaseModel, ConfigDict

class FoodBase(BaseModel):
    name: str
    unit: str
    calories: float
    category: str

class FoodCreate(FoodBase):
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Banane",
                "unit": "g",
                "calories": 2.1
            }
        }
    }

class FoodOut(FoodBase):
    id: int
    
    model_config = ConfigDict(from_attributes = True)