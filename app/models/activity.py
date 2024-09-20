from sqlalchemy import Column, String, Integer, Float, Date, Time, ForeignKey
from ..db.base import Base

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    activity_type = Column(String, nullable=False)
    duration = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
