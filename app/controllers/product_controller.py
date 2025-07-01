from flask import request, jsonify
from app.repositories.product_repository import ProductRepository

class ProductController:
    def __init__(self):
        self.repository = ProductRepository()
    
    def get_all_products(self):
        """GET /products - Lista todos os produtos"""
        try:
            category = request.args.get('category')
            search = request.args.get('search')
            
            if category:
                products = self.repository.get_by_category(category)
            elif search:
                products = self.repository.search(search)
            else:
                products = self.repository.get_all()
            
            return jsonify({
                'success': True,
                'data': [product.to_dict() for product in products],
                'count': len(products)
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    def get_product(self, product_id):
        """GET /products/<id> - Busca um produto por ID"""
        try:
            product = self.repository.get_by_id(product_id)
            if not product:
                return jsonify({
                    'success': False,
                    'error': 'Produto não encontrado'
                }), 404
            
            return jsonify({
                'success': True,
                'data': product.to_dict()
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    def create_product(self):
        """POST /products - Cria um novo produto"""
        try:
            data = request.get_json()
            
            # Validação dos campos obrigatórios
            required_fields = ['name', 'description', 'price', 'category']
            for field in required_fields:
                if field not in data:
                    return jsonify({
                        'success': False,
                        'error': f'Campo obrigatório ausente: {field}'
                    }), 400
            
            # Validação de tipos
            if not isinstance(data['price'], (int, float)) or data['price'] < 0:
                return jsonify({
                    'success': False,
                    'error': 'Preço deve ser um número positivo'
                }), 400
            
            stock = data.get('stock', 0)
            if not isinstance(stock, int) or stock < 0:
                return jsonify({
                    'success': False,
                    'error': 'Estoque deve ser um número inteiro positivo'
                }), 400
            
            product = self.repository.create(
                name=data['name'],
                description=data['description'],
                price=float(data['price']),
                category=data['category'],
                stock=stock
            )
            
            return jsonify({
                'success': True,
                'data': product.to_dict(),
                'message': 'Produto criado com sucesso'
            }), 201
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    def update_product(self, product_id):
        """PUT /products/<id> - Atualiza um produto"""
        try:
            data = request.get_json()
            
            # Validação de preço se fornecido
            if 'price' in data:
                if not isinstance(data['price'], (int, float)) or data['price'] < 0:
                    return jsonify({
                        'success': False,
                        'error': 'Preço deve ser um número positivo'
                    }), 400
                data['price'] = float(data['price'])
            
            # Validação de estoque se fornecido
            if 'stock' in data:
                if not isinstance(data['stock'], int) or data['stock'] < 0:
                    return jsonify({
                        'success': False,
                        'error': 'Estoque deve ser um número inteiro positivo'
                    }), 400
            
            product = self.repository.update(product_id, **data)
            if not product:
                return jsonify({
                    'success': False,
                    'error': 'Produto não encontrado'
                }), 404
            
            return jsonify({
                'success': True,
                'data': product.to_dict(),
                'message': 'Produto atualizado com sucesso'
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    def delete_product(self, product_id):
        """DELETE /products/<id> - Remove um produto"""
        try:
            success = self.repository.delete(product_id)
            if not success:
                return jsonify({
                    'success': False,
                    'error': 'Produto não encontrado'
                }), 404
            
            return jsonify({
                'success': True,
                'message': 'Produto removido com sucesso'
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500