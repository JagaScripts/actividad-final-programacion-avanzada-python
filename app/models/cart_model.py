# app/models/cart_model.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .dec_base import DecBase

class CartItem(DecBase):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, default=1)
    owner_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    owner = relationship("User", back_populates="cart_items")
    product = relationship("Product")