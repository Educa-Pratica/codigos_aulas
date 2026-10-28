# codigos_aulas

Códigos e notebooks utilizados nas aulas do canal [Educa Prática](https://github.com/Educa-Pratica).

Repositório com exemplos práticos de **IA agêntica**, **LLMs locais e embeddings**, **deploy na nuvem com Modal**, **simulação de Monte Carlo** e **geração automática de slides**, todos acompanhados nos vídeos do canal.

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
  - [`dimulacao_monte_carlo/figurinhas_copa.ipynb`](dimulacao_monte_carlo/figurinhas_copa.ipynb) — aplicação prática: estimar quantas figurinhas da Copa são necessárias para completar o álbum usando simulações.
  - [`dimulacao_monte_carlo/yt_sim_carlo.ipynb`](dimulacao_monte_carlo/yt_sim_carlo.ipynb) — exemplo usado no vídeo do YouTube sobre simulação de Monte Carlo.

---

### 🏆 Previsão da Copa do Mundo 2026

Modelo de Machine Learning para prever o campeão da Copa do Mundo de 2026 com base em dados históricos de seleções.

- **Notebook:** [`previsao_wc_2026/previsao_copa_26.ipynb`](previsao_wc_2026/previsao_copa_26.ipynb)
- **Dados:** [`previsao_wc_2026/features_wc.csv`](previsao_wc_2026/features_wc.csv)
- **Stack:** Python, Pandas, NumPy, Scikit-learn
- **Como funciona:**
  1. Carrega features históricas de seleções desde copas anteriores (ELO rating, ranking FIFA, títulos, ataque, defesa, meio-campo, desempenho recente em jogos).
  2. Treina e compara múltiplos classificadores (RandomForest, GradientBoosting, AdaBoost, ExtraTrees, MLP, SVC) com validação cruzada.
  3. Seleciona o melhor modelo e gera probabilidades de vitória para cada seleção na Copa de 2026.

---

### 🧠 EmbeddingGemma 2 — Embeddings na prática

Notebook introdutório ao modelo de embeddings **EmbeddingGemma 2** do Google, mostrando o que são embeddings e suas principais aplicações.

- **Notebook:** [`gemmaembeddings/embeddinggemma2_exemplos.ipynb`](gemmaembeddings/embeddinggemma2_exemplos.ipynb)
- **Recursos de exemplo:** [`gemmaembeddings/praia.jpg`](gemmaembeddings/praia.jpg), [`gemmaembeddings/montanha.jpg`](gemmaembeddings/montanha.jpg), [`gemmaembeddings/pug.jpg`](gemmaembeddings/pug.jpg)
- **Stack:** Python, sentence-transformers, transformers
- **Como funciona:**
  1. Carrega o modelo apenas com os recursos de texto e código (≈270M parâmetros).
  2. Gera o primeiro embedding e calcula similaridade de cosseno entre textos.
  3. Demonstra uma mini busca semântica e classificação por similaridade (`prompt_name="Classification"`) sem treinar um classificador.
  4. Explora a técnica **Matryoshka** (comparar 768, 256 e 128 dimensões) e busca em código por linguagem natural.
  5. Opcional: busca de imagens a partir de texto (cross-modal retrieval), carregando os recursos de visão (≈440M parâmetros).

---

### 💻 LLMs locais

Exemplo de como chamar um **LLM rodando localmente** através de um endpoint compatível com a API da OpenAI.

- **Notebook:** [`llm_locais/chamada.ipynb`](llm_locais/chamada.ipynb)
- **Stack:** LangChain (`init_chat_model`), servidor local compatível com OpenAI (`http://127.0.0.1:8080/v1`)
- **Como funciona:**
  1. Sobem um modelo no formato GGUF (ex.: `Bielik-Minitron-7B`) em um servidor local expondo a API da OpenAI.
  2. Usam `init_chat_model` do LangChain apontando `base_url` para o servidor local.
  3. Enviam um prompt e imprimem a resposta gerada — tudo sem depender de serviços na nuvem.

---

### 🤏 Laya — Decisões estruturadas vs. classificadores clássicos

Comparação de abordagens para **classificação de sentimento** (positivo/negativo) em avaliações de produtos em português.

- **Notebooks:**
  - [`laya/Testando_o_Laya.ipynb`](laya/Testando_o_Laya.ipynb) — compara a abordagem clássica supervisionada (TF-IDF + Regressão Logística) com APIs de "decisões" estruturadas (Jev, OpenAI Decisions) e com a lib `laya`.
  - [`laya/Testando_o_OADecisions.ipynb`](laya/Testando_o_OADecisions.ipynb) — foca no uso das APIs de decisão estruturada e do `laya.Router` para responder perguntas do tipo `choice`.
- **Dados:** [`laya/class.xlsx`](laya/class.xlsx)
- **Stack:** Python, scikit-learn, NLTK, pandas, `laya`, OpenRouter
- **Como funciona:**
  1. Carrega a base de reviews rotulados (`class.xlsx`).
  2. Treina um baseline clássico com TF-IDF + Regressão Logística.
  3. Define uma pergunta estruturada (`{"type": "choice", ...}`) e a responde via Jev, OpenAI Decisions e `laya.Router` (`router.predict`).
  4. Compara os `classification_report`s de cada abordagem.

---

### 🖼️ Criar Slides — Geração automática de apresentações

Gera as imagens de um slide deck com a API do **GPT-Image-2** (via OpenRouter) e monta automaticamente um arquivo **.pptx** pronto para apresentar.

- **Notebook:** [`criarSlides/gerar_slides.ipynb`](criarSlides/gerar_slides.ipynb)
- **Descrições de entrada:** [`criarSlides/slides_descricao.md`](criarSlides/slides_descricao.md)
- **Exemplo gerado:** [`criarSlides/apresentacao.pptx`](criarSlides/apresentacao.pptx)
- **Stack:** Python, requests, python-pptx, python-dotenv
- **Como funciona:**
  1. Lê a descrição de cada slide a partir de um arquivo `.md`.
  2. Gera cada imagem de slide com o modelo `openai/gpt-image-2` (proporção 16:9) e salva em `criarSlides/imagens/`.
  3. Lê as imagens geradas e monta o `.pptx` com `python-pptx`.
- **Observação:** requer a variável `OPENROUTER_API_KEY` definida no arquivo `.env`.

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