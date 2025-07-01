import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from app.controllers.product_controller import ProductController

@pytest.fixture
def app():
    app = Flask(__name__)
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()

@pytest.fixture
def controller():
    return ProductController()

@patch('app.controllers.product_controller.ProductRepository')
def test_get_all_products(MockRepo, app, controller):
    mock_repo = MockRepo.return_value
    mock_product = MagicMock()
    mock_product.to_dict.return_value = {'id': 1, 'name': 'Produto Teste'}
    mock_repo.get_all.return_value = [mock_product]
    controller.repository = mock_repo
    with app.test_request_context('/products'):
        response, status_code = controller.get_all_products()
        data = response.get_json()
    assert status_code == 200
    assert data['success']
    assert data['count'] == 1
    assert data['data'][0]['name'] == 'Produto Teste'

@patch('app.controllers.product_controller.ProductRepository')
def test_get_product(MockRepo, app, controller):
    mock_repo = MockRepo.return_value
    mock_product = MagicMock()
    mock_product.to_dict.return_value = {'id': 1, 'name': 'Produto Teste'}
    mock_repo.get_by_id.return_value = mock_product
    controller.repository = mock_repo
    with app.test_request_context('/products/1'):
        response, status_code = controller.get_product(1)
        data = response.get_json()
    assert status_code == 200
    assert data['success']
    assert data['data']['name'] == 'Produto Teste'

@patch('app.controllers.product_controller.ProductRepository')
def test_create_product(MockRepo, app, controller):
    mock_repo = MockRepo.return_value
    mock_product = MagicMock()
    mock_product.to_dict.return_value = {'id': 1, 'name': 'Produto Teste'}
    mock_repo.create.return_value = mock_product
    controller.repository = mock_repo
    payload = {
        'name': 'Produto Teste',
        'description': 'Desc',
        'price': 10.0,
        'category': 'Teste',
        'stock': 5
    }
    with app.test_request_context('/products', method='POST', json=payload):
        response, status_code = controller.create_product()
        data = response.get_json()
    assert status_code == 201
    assert data['success']
    assert data['data']['name'] == 'Produto Teste'
    assert data['message'] == 'Produto criado com sucesso'

@patch('app.controllers.product_controller.ProductRepository')
def test_update_product(MockRepo, app, controller):
    mock_repo = MockRepo.return_value
    mock_product = MagicMock()
    mock_product.to_dict.return_value = {'id': 1, 'name': 'Produto Atualizado'}
    mock_repo.update.return_value = mock_product
    controller.repository = mock_repo
    payload = {'name': 'Produto Atualizado', 'price': 20.0}
    with app.test_request_context('/products/1', method='PUT', json=payload):
        response, status_code = controller.update_product(1)
        data = response.get_json()
    assert status_code == 200
    assert data['success']
    assert data['data']['name'] == 'Produto Atualizado'
    assert data['message'] == 'Produto atualizado com sucesso'

@patch('app.controllers.product_controller.ProductRepository')
def test_delete_product(MockRepo, app, controller):
    mock_repo = MockRepo.return_value
    mock_repo.delete.return_value = True
    controller.repository = mock_repo
    with app.test_request_context('/products/1', method='DELETE'):
        response, status_code = controller.delete_product(1)
        data = response.get_json()
    assert status_code == 200
    assert data['success']
    assert data['message'] == 'Produto removido com sucesso'
