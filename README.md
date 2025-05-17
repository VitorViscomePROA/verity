# Desafio SQL Agent – Verity

Este projeto implementa um agente LLM que converte linguagem natural em SQL, executa as queries em um banco PostgreSQL e retorna os resultados formatados. Ele foi desenvolvido como parte de um desafio técnico e utiliza **LangChain**, **LangGraph**, **Ollama (modelo local)** e **PostgreSQL via Docker**.

---

## 🧠 Tecnologias

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://ollama.com/) com modelo `mistral`
- PostgreSQL via Docker
- SQLAlchemy + Pandas
- UX: Yaspin (spinners CLI)

---

## 🛠 Comandos via Makefile

Você pode usar os seguintes comandos para facilitar o uso do projeto:

```bash
make venv        # Cria e configura o ambiente virtual #
make db-up       # Sobe o banco PostgreSQL via Docker #
make ollama      # Inicia o modelo local mistral #
make run         # Executa o agente conversacional #
make test-db     # Testa conexão com o banco #


## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/VitorViscomePROA/verity.git
cd desafio-verity
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Suba o banco de dados PostgreSQL

```bash
docker-compose up -d
```

O script de inicialização (`postgres-init`) vai criar as tabelas e dados automaticamente.

---

### 5. Inicie o modelo local via Ollama

```bash
ollama run mistral
```

Certifique-se de que o Ollama esteja instalado: [https://ollama.com/download](https://ollama.com/download)

---

### 6. Execute o agente

```bash
python src/langgraph_flow.py
```

Digite uma pergunta como:

```
quem comprou smartphones?
```

---

## 💬 Exemplo

**Input:**
```
quem comprou smartphones?
```

**SQL gerada:**
```sql
SELECT clientes.nome
FROM clientes
JOIN transacoes ON clientes.id = transacoes.cliente_id
JOIN produtos ON transacoes.produto_id = produtos.id
WHERE produtos.nome ILIKE '%smartphone%';
```

**Resultado:**
```
    nome
Bruno Lima
```

---

## ⚠️ Observações Técnicas

- Usamos `sqlalchemy.text()` para evitar erros com `immutabledict` na integração Pandas + SQLAlchemy 2.x
- O fluxo de execução é gerenciado via `LangGraph` com estados:
  - `gerar_sql`
  - `executar_sql`
- Todo processamento ocorre localmente com o modelo Mistral via Ollama

---

## 📁 Estrutura

```
desafio_verity/
├── docker-compose.yml
├── postgres-init/
├── requirements.txt
├── src/
│   ├── db.py
│   ├── langgraph_flow.py
│   └── prompt_context.txt
```

---

## ✅ Requisitos

- Python 3.10+
- Docker
- Ollama (com o modelo `mistral` instalado)

---

## 📬 Contato

Este projeto foi desenvolvido como parte de um desafio técnico.  
Dúvidas ou sugestões? Fique à vontade para entrar em contato via WhatsApp (11)98570-2857
