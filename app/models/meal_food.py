from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from ..db.base import Base

class MealFood(Base):
    __tablename__ = "meal_foods"

    id = Column(Integer, primary_key=True, index=True)
    meal_id = Column(Integer, ForeignKey('meals.id'))
    food_id = Column(Integer, ForeignKey('foods.id'))
    quantity = Column(Float, nullable=False)

    # Meal relationship
    meals = relationship("Meal", back_populates="foods")

    # food relationship
    foods = relationship("Food", back_populates="meals")
