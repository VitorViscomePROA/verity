from langgraph.graph import StateGraph
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableLambda
from langchain.prompts import PromptTemplate
from db import executar_sql
from typing import TypedDict
from yaspin import yaspin

# === SCHEMA DO ESTADO ===
class GraphState(TypedDict, total=False):
    pergunta: str
    sql: str
    resultado: str
    erro: str

# === PROMPT + LLM ===
with open("src/prompt_context.txt", "r", encoding="utf-8") as f:
    contexto = f.read()

prompt = PromptTemplate(
    input_variables=["pergunta"],
    template=f"""{contexto}

Usuário perguntou: "{{pergunta}}"
Responda apenas com a query SQL correspondente, sem explicações.
"""
)

llm = ChatOllama(model="mistral", temperature=0)

# === FUNÇÕES DOS NÓS ===

def gerar_sql(state: GraphState) -> GraphState:
    pergunta = state["pergunta"]
    with yaspin(text="🔄 Gerando SQL...", color="cyan"):
        resposta = (prompt | llm).invoke({"pergunta": pergunta})
        sql = resposta.content.strip()
    return {"sql": sql}

def executar(state: GraphState) -> GraphState:
    try:
        with yaspin(text="⏳ Executando consulta no banco...", color="yellow"):
            sql_final = state["sql"]
            print(f"\n🧪 DEBUG: tipo da SQL recebida => {type(sql_final)}")
            print(f"🧪 Conteúdo: {sql_final}")

            df = executar_sql(sql_final)

        return {"resultado": df.to_string(index=False)}
    except Exception as e:
        return {"erro": str(e)}

# === GRAFO ===

workflow = StateGraph(GraphState)
workflow.add_node("gerar_sql", RunnableLambda(gerar_sql))
workflow.add_node("executar_sql", RunnableLambda(executar))
workflow.set_entry_point("gerar_sql")
workflow.add_edge("gerar_sql", "executar_sql")
workflow.set_finish_point("executar_sql")
graph_app = workflow.compile()

# === EXECUÇÃO FINAL ===

if __name__ == "__main__":
    pergunta = input("Faça uma pergunta: ")
    result = graph_app.invoke({"pergunta": pergunta})

    print("\n🔍 SQL gerada:")
    print(result.get("sql"))

    if "erro" in result:
        print("\n❌ Erro ao executar SQL:")
        print(result["erro"])
    else:
        print("\n📊 Resultado:")
        print(result["resultado"])
