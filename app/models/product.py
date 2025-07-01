from datetime import datetime
from typing import Optional

class Product:
    def __init__(self, id: int, name: str, description: str, price: float, category: str, stock: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock = stock
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'stock': self.stock,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    def update(self, name: Optional[str] = None, description: Optional[str] = None, 
               price: Optional[float] = None, category: Optional[str] = None, 
               stock: Optional[int] = None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        if category is not None:
            self.category = category
        if stock is not None:
            self.stock = stock
        self.updated_at = datetime.now()