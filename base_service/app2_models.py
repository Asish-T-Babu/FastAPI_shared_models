# shared_models/app1_models.py
from sqlalchemy import Column, Integer, String, ForeignKey

from base_service.base import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

