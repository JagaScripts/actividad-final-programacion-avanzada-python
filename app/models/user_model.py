# app/models/user_model.py

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    """
    Modelo SQLAlchemy que representa la tabla 'users'.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    # Relación con el carrito de compras
    # Un usuario puede tener varios items en su carrito
    cart_items = relationship("CartItem", back_populates="owner")