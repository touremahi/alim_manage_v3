from sqlalchemy import (
    Column, Integer, Float, String
)
from sqlalchemy.orm import relationship
from ..db.base import Base

class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    unit = Column(String, nullable=False)
    calories = Column(Float, nullable=False)
    category = Column(String)

    meals = relationship("MealFood", back_populates="foods")