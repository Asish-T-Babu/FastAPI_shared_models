# shared_models/app1_models.py
from sqlalchemy import Column, Integer, String

from base_service.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
