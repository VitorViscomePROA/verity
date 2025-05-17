# Makefile para facilitar a execução do projeto

# ⚙️ Setup do ambiente
venv:
	python -m venv venv
	venv\Scripts\activate && pip install -r requirements.txt

# 🐘 Banco de dados
db-up:
	docker-compose up -d

db-down:
	docker-compose down

# 🤖 Modelo local
ollama:
	ollama run mistral

# 🚀 Executar o agente
run:
	venv\Scripts\activate && python src/langgraph_flow.py

# 🧪 Teste de conexão com banco
test-db:
	venv\Scripts\activate && python -c "from db import executar_sql; print(executar_sql('SELECT * FROM clientes LIMIT 1'))"
