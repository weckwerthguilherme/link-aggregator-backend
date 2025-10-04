from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy import func
from .database import Base

class Link(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    url = Column(Text, nullable=False)
    display_order = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
