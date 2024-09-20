from sqlalchemy import Column, Integer, Date, Float, ForeignKey
from ..db.base import Base

class Weight(Base):
    __tablename__ = "weights"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    weight = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
