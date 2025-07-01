from typing import List, Optional
from app.models.product import Product

class ProductRepository:
    def __init__(self):
        self._products = {}
        self._next_id = 1
        self._seed_data()
    
    def _seed_data(self):
        """Adiciona alguns produtos iniciais para teste"""
        initial_products = [
            Product(1, "Smartphone", "Smartphone Android com 128GB", 899.99, "Eletrônicos", 50),
            Product(2, "Notebook", "Notebook Intel i5 8GB RAM", 2499.99, "Eletrônicos", 25),
            Product(3, "Camiseta", "Camiseta 100% algodão", 39.99, "Roupas", 100),
            Product(4, "Tênis", "Tênis esportivo confortável", 199.99, "Calçados", 75)
        ]
        
        for product in initial_products:
            self._products[product.id] = product
            if product.id >= self._next_id:
                self._next_id = product.id + 1
    
    def create(self, name: str, description: str, price: float, category: str, stock: int = 0) -> Product:
        product = Product(self._next_id, name, description, price, category, stock)
        self._products[self._next_id] = product
        self._next_id += 1
        return product
    
    def get_all(self) -> List[Product]:
        return list(self._products.values())
    
    def get_by_id(self, product_id: int) -> Optional[Product]:
        return self._products.get(product_id)
    
    def get_by_category(self, category: str) -> List[Product]:
        return [product for product in self._products.values() if product.category.lower() == category.lower()]
    
    def update(self, product_id: int, **kwargs) -> Optional[Product]:
        product = self._products.get(product_id)
        if product:
            product.update(**kwargs)
            return product
        return None
    
    def delete(self, product_id: int) -> bool:
        if product_id in self._products:
            del self._products[product_id]
            return True
        return False
    
    def search(self, query: str) -> List[Product]:
        """Busca produtos por nome ou descrição"""
        query = query.lower()
        return [
            product for product in self._products.values()
            if query in product.name.lower() or query in product.description.lower()
        ]