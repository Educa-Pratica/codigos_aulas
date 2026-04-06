# codigos_aulas

Códigos e notebooks usados nas aulas do canal [Educa Prática](https://github.com/Educa-Pratica).

## Projetos

### Agente Text-to-SQL

Agente de IA que converte perguntas em linguagem natural para consultas SQL e retorna as respostas a partir de um banco de dados.

- **Notebook:** [`agente_txt_to_sql/codigo.ipynb`](agente_txt_to_sql/codigo.ipynb)
- **Stack:** LangChain, LangGraph, SQLAlchemy, Pandas, Groq
- **Como funciona:**
  1. Configura um LLM (via Groq) como cérebro do agente.
  2. Carrega dados de um arquivo Excel para um banco SQLite em memória.
  3. Utiliza o `SQLDatabaseToolkit` do LangChain como ferramentas do agente.
  4. Cria um fluxo agêntico com `create_agent` que recebe a pergunta do usuário, gera e executa a consulta SQL, e retorna a resposta.
