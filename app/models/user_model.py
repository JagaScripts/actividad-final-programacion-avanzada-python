# app/models/user_model.py

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .dec_base import DecBase

class User(DecBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    cart_items = relationship("CartItem", back_populates="owner")