from sqlalchemy import Column, Integer, String, Float, Boolean
from ..db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    age = Column(Integer)
    initial_weight = Column(Float)
    is_active = Column(Boolean, default=True)
