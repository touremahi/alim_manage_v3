from sqlalchemy import (
    Column, Integer, String, Date, Time, Float, Boolean,
    ForeignKey
)
from sqlalchemy.orm import relationship

from ..db.base import Base

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    date = Column(Date)
    time = Column(Time)
    user_id = Column(Integer, ForeignKey('users.id'))

    foods = relationship("MealFood", back_populates="meals")
