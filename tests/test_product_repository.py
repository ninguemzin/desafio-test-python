import pytest
from app.repositories.product_repository import ProductRepository

@pytest.fixture
def repo():
    return ProductRepository()

def test_seed_data(repo):
    products = repo.get_all()
    assert len(products) == 4
    names = [p.name for p in products]
    assert 'Smartphone' in names
    assert 'Notebook' in names
    assert 'Camiseta' in names
    assert 'Tênis' in names

def test_create_product(repo):
    product = repo.create('Mouse', 'Mouse óptico', 50.0, 'Eletrônicos', 10)
    assert product.id == 5
    assert product.name == 'Mouse'
    assert repo.get_by_id(product.id) == product

def test_get_by_id(repo):
    product = repo.get_by_id(1)
    assert product is not None
    assert product.name == 'Smartphone'
    assert repo.get_by_id(999) is None

def test_get_by_category(repo):
    eletr = repo.get_by_category('Eletrônicos')
    assert len(eletr) == 2
    assert all(p.category == 'Eletrônicos' for p in eletr)

def test_update_product(repo):
    product = repo.create('Teclado', 'Teclado mecânico', 200.0, 'Eletrônicos', 5)
    updated = repo.update(product.id, name='Teclado Gamer', price=250.0)
    assert updated is not None
    assert updated.name == 'Teclado Gamer'
    assert updated.price == 250.0
    assert repo.update(999, name='Nada') is None

def test_delete_product(repo):
    product = repo.create('Fone', 'Fone bluetooth', 120.0, 'Eletrônicos', 3)
    assert repo.delete(product.id) is True
    assert repo.get_by_id(product.id) is None
    assert repo.delete(999) is False

def test_search(repo):
    results = repo.search('notebook')
    assert len(results) == 1
    assert results[0].name == 'Notebook'
    results = repo.search('algodão')
    assert len(results) == 1
    assert results[0].name == 'Camiseta'
    results = repo.search('inexistente')
    assert results == []
