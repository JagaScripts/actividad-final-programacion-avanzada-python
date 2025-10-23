from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Dict, Any, Optional

class CartBase(BaseModel):
    user_id: int = Field(..., gt=0, description="User ID")
    date: datetime = Field(..., description="Cart date")

class CartCreate(CartBase):
    products: List[Dict[str, Any]] = Field(..., description="List of products with quantities")

class CartUpdate(BaseModel):
    user_id: Optional[int] = Field(None, gt=0, description="User ID")
    date: Optional[datetime] = Field(None, description="Cart date")
    products: Optional[List[Dict[str, Any]]] = Field(None, description="List of products with quantities")

class CartResponse(CartBase):
    id: int = Field(..., description="Cart ID")
    products: List[Dict[str, Any]] = Field(..., description="List of products with quantities")

    class Config:
        from_attributes = True