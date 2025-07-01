# API de Produtos - Flask

API REST simples com **Python** + **Flask** para CRUD de produtos, usando armazenamento em memória. Projeto organizado em camadas (models, repositories, controllers) e com testes unitários em **pytest**.

## 📁 Estrutura

app/
controllers/
models/
repositories/
routes.py
run.py
tests/
requirements.txt

## ▶️ Como rodar

```bash
pip install -r requirements.txt
python run.py

🧪 Testes
bash
Copiar código
pip install pytest
pytest tests/
Se necessário:

bash
Copiar código
export PYTHONPATH=.
🔗 Endpoints
GET /products

GET /products/<id>

POST /products

PUT /products/<id>

DELETE /products/<id>

⚠️ Observações
Dados não persistem (tudo em memória)

Foco didático: APIs, Flask, testes
```
