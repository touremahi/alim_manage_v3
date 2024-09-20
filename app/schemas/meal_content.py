from typing import List

from pydantic import BaseModel

from .meal import MealOut

class MealFoodOutCalories(BaseModel):
    id: int
    name: str
    category : str
    quantity: float
    calories: float = 0.0

class MealContentOut(MealOut):
    foods: List[MealFoodOutCalories]

