# app/models/cart_model.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class CartItem(Base):
    """
    Modelo SQLAlchemy que representa un item en el carrito de un usuario.
    """
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, default=1)

    # Clave foránea para relacionar con el usuario
    owner_id = Column(Integer, ForeignKey("users.id"))
    # Clave foránea para relacionar con el producto
    product_id = Column(Integer, ForeignKey("products.id"))

    # Relación para poder acceder al objeto User completo desde un CartItem
    owner = relationship("User", back_populates="cart_items")
    # Relación para poder acceder al objeto Product completo desde un CartItem
    product = relationship("Product")