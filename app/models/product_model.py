# app/models/product_model.py

from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class Product(Base):
    """
    Modelo SQLAlchemy que representa la tabla 'products'.
    """
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    price = Column(Float)
    description = Column(String)
    category = Column(String)
    image = Column(String)
    rating_rate = Column(Float)
    rating_count = Column(Integer)