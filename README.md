# codigos_aulas

Códigos e notebooks utilizados nas aulas do canal [Educa Prática](https://github.com/Educa-Pratica).

Repositório com exemplos práticos de **IA agêntica**, **deploy na nuvem com Modal** e **simulação de Monte Carlo**, todos acompanhados nos vídeos do canal.

---

## 📂 Projetos

### 🤖 Agente Text-to-SQL

Agente de IA que converte perguntas em linguagem natural para consultas SQL e retorna as respostas a partir de um banco de dados.

- **Notebook:** [`agente_txt_to_sql/codigo.ipynb`](agente_txt_to_sql/codigo.ipynb)
- **Stack:** LangChain, LangGraph, SQLAlchemy, Pandas, Groq
- **Como funciona:**
  1. Configura um LLM (via Groq) como cérebro do agente.
  2. Carrega dados de um arquivo Excel (`agente_txt_to_sql/dados/dados.xlsx`) para um banco SQLite em memória.
  3. Utiliza o `SQLDatabaseToolkit` do LangChain como ferramentas do agente.
  4. Cria um fluxo agêntico com `create_agent` que recebe a pergunta do usuário, gera e executa a consulta SQL e retorna a resposta em linguagem natural.

---

### ☁️ Deploy com Modal

Cron job rodando na nuvem que consulta cotações de ações da B3 em intervalos regulares usando o [Modal](https://modal.com/).

- **Arquivo principal:** [`deploy_modal/main.py`](deploy_modal/main.py)
- **Utilitários:** [`deploy_modal/utils/utils.py`](deploy_modal/utils/utils.py)
- **Stack:** Modal, yfinance, requests
- **Como funciona:**
  1. Define uma imagem customizada (`modal.Image.debian_slim()`) com as dependências (`requests`, `yfinance`) e o diretório `utils/`.
  2. Cria um `App` no Modal (`Video_YT`).
  3. Agenda a função `main` com `@app.function(schedule=modal.Period(seconds=30))`, que chama `get_stock_info()` para imprimir preço, variação, abertura, máxima e mínima dos tickers configurados (por padrão `PETR3.SA` e `PETR4.SA`).
- **Como rodar localmente (passo a passo, conforme comentários no `main.py`):**
  1. Criar conta no Modal.
  2. `pip install modal`
  3. Gerar token com `modal token new`.
  4. `modal run deploy_modal/main.py` (testa localmente na nuvem).
  5. `modal deploy deploy_modal/main.py` (implanta o cron job).

---

### 🎲 Simulação de Monte Carlo

Conjunto de notebooks explicando o que é simulação e a técnica de Monte Carlo, com aplicações práticas.

- **Stack:** Python, NumPy, Pandas, Matplotlib
- **Notebooks:**
  - [`dimulacao_monte_carlo/simulacao_monte_carlo.ipynb`](dimulacao_monte_carlo/simulacao_monte_carlo.ipynb) — aula completa, do conceito à prática: o que é simulação, para que serve (e para que **não** serve), com exemplos e visualizações.
  - [`dimulacao_monte_carlo/aula_sim_monte_carlo.ipynb`](dimulacao_monte_carlo/aula_sim_monte_carlo.ipynb) — versão enxuta da aula, ideal para revisão rápida.
  - [`dimulacao_monte_carlo/figurinhas_copa.ipynb`](dimulacao_monte_carlo/figurinhas_copa.ipynb) — aplicação prática: estimar quantas figurinhas da Copa são necessárias para completar o álbum usando simulações.
  - [`dimulacao_monte_carlo/yt_sim_carlo.ipynb`](dimulacao_monte_carlo/yt_sim_carlo.ipynb) — exemplo usado no vídeo do YouTube sobre simulação de Monte Carlo.

---

## 🚀 Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Educa-Pratica/codigos_aulas.git
   cd codigos_aulas
   ```
2. Abra os notebooks no **VS Code** (com a extensão Jupyter) ou no **Jupyter Notebook/Lab**.
3. Para o projeto de deploy, siga o passo a passo indicado em [`deploy_modal/main.py`](deploy_modal/main.py).

---

## 📺 Canal

Acompanhe as aulas no canal **Educa Prática** para entender cada projeto em detalhes:
- GitHub: [Educa-Pratica](https://github.com/Educa-Pratica)