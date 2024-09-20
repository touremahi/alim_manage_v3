from datetime import date, time, timedelta
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr

from .meal import MealOut
from .food import FoodOut

class MealFoodBase(BaseModel):
    meals: MealOut
    foods: FoodOut
    quantity: float

class MealFoodCreate(MealFoodBase):
    pass

class MealFoodUpdate(BaseModel):
    meal_id: int
    food_id: int
    quantity: float

class MealFoodOut(MealFoodBase):
    id: int

    model_config = ConfigDict(from_attributes = True)
