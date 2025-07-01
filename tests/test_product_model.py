import pytest
from datetime import datetime, timedelta
import time
from app.models.product import Product

def test_product_to_dict():
    product = Product(1, 'Produto', 'Descrição', 10.0, 'Categoria', 5)
    result = product.to_dict()
    assert result['id'] == 1
    assert result['name'] == 'Produto'
    assert result['description'] == 'Descrição'
    assert result['price'] == 10.0
    assert result['category'] == 'Categoria'
    assert result['stock'] == 5
    # Verifica se as datas estão no formato ISO
    assert 'T' in result['created_at']
    assert 'T' in result['updated_at']

def test_product_update():
    product = Product(1, 'Produto', 'Descrição', 10.0, 'Categoria', 5)
    old_updated_at = product.updated_at
    time.sleep(0.001)  # Garante diferença de tempo
    product.update(name='Novo', price=20.0, stock=10)
    assert product.name == 'Novo'
    assert product.price == 20.0
    assert product.stock == 10
    assert product.updated_at > old_updated_at

def test_product_update_partial():
    product = Product(1, 'Produto', 'Descrição', 10.0, 'Categoria', 5)
    product.update()
    # Não deve alterar nada
    assert product.name == 'Produto'
    assert product.price == 10.0
    assert product.stock == 5
