from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # Configurações
    app.config['JSON_SORT_KEYS'] = False
    
    # CORS para permitir requisições de diferentes origens
    CORS(app)
    
    # Registrar blueprints
    from app.routes import api
    app.register_blueprint(api)
    
    # Rota de health check
    @app.route('/health')
    def health_check():
        return {'status': 'OK', 'message': 'API funcionando corretamente'}
    
    # Rota raiz
    @app.route('/')
    def index():
        return {
            'message': 'API de Produtos - Flask Backend',
            'version': '1.0.0',
            'endpoints': {
                'GET /health': 'Health check',
                'GET /api/products': 'Listar todos os produtos',
                'GET /api/products?category=<categoria>': 'Filtrar por categoria',
                'GET /api/products?search=<termo>': 'Buscar produtos',
                'GET /api/products/<id>': 'Buscar produto por ID',
                'POST /api/products': 'Criar novo produto',
                'PUT /api/products/<id>': 'Atualizar produto',
                'DELETE /api/products/<id>': 'Remover produto'
            }
        }
    
    return app