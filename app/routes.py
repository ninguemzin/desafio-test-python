from flask import Blueprint
from app.controllers.product_controller import ProductController

# Criar blueprint para as rotas
api = Blueprint('api', __name__, url_prefix='/api')

# Instanciar o controller
product_controller = ProductController()

# Rotas dos produtos
api.add_url_rule('/products', 'get_products', product_controller.get_all_products, methods=['GET'])
api.add_url_rule('/products', 'create_product', product_controller.create_product, methods=['POST'])
api.add_url_rule('/products/<int:product_id>', 'get_product', product_controller.get_product, methods=['GET'])
api.add_url_rule('/products/<int:product_id>', 'update_product', product_controller.update_product, methods=['PUT'])
api.add_url_rule('/products/<int:product_id>', 'delete_product', product_controller.delete_product, methods=['DELETE'])