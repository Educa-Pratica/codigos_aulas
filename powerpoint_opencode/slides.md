# Slides — Agentes de IA

Arquivo de **descrição e instruções** para gerar 5 slides sobre agentes de IA.

- **Tema:** o que são agentes de IA, como funcionam, tipos, aplicações e cuidados.
- **Público:** executivo / técnico iniciante — apresentação didática e de alto nível.
- **Formato:** 16:9 (1920×1080 px).
- **Uso:** lido por um notebook de geração de imagens (ex.: `criarSlides/gerar_slides.ipynb`, modelo `openai/gpt-image-2`) ou usado como roteiro para montar o `.pptx` manualmente.

---

## Instruções gerais (valem para os 5 slides)

- **Referência de estilo obrigatória:** seguir `powerpoint_opencode/estilos/DESIGN_SYSTEM_SLIDES.md`.
- **Paleta:** fundo `#FFFFFF` / `#F7F8FA`; texto `#111827` e `#4B5563`; borda `#E5E7EB`; destaque `#2563EB` (azul), `#1D4ED8`, fundo suave `#DBEAFE`; apoio `#16A34A` (verde), `#D97706` (amarelo), `#DC2626` (vermelho).
- **Tipografia:** Inter (fallback Aptos/Manrope). Título do slide 36–48 pt; corpo 18–24 pt; KPI 48–72 pt; legenda 12–16 pt. Peso 700 em títulos, 400 no corpo.
- **Espaçamento:** múltiplos de 8 (8/16/24/32/48/64). Margens: 96 px laterais, 72 px topo/base.
- **Regra 70/20/10:** maioria neutra + espaço em branco, estrutura em texto, destaque azul só no que importa.
- **Ícones:** usar **somente** os SVGs de `powerpoint_opencode/estilos/icones_design_system_slides/icons/` (outline, 24×24, stroke 1.8, `currentColor`). Disponíveis: `ai`, `analytics`, `arrow-right`, `chart-bar`, `chart-line`, `check`, `cloud`, `database`, `globe`, `lightbulb`, `lock`, `people`, `rocket`, `settings`, `target`, `trend-up`, `warning`. Não misturar estilos.
- **Títulos:** devem comunicar uma conclusão/insight, nunca apenas o assunto.
- **Consistência:** mesmo cabeçalho, mesma posição de título, mesmo estilo de card/caixa nos 5 slides. Sem sombras fortes, sem gradientes, sem gráficos 3D.

---

## Slide 1 — Capa + definição

**Mensagem-chave:** um agente de IA não apenas responde — ele **age** para atingir um objetivo.

**Prompt de geração:**
Crie um slide de capa limpo, muito espaço em branco. Fundo branco com um detalhe geométrico sutil em azul claro (`#DBEAFE`) no canto superior esquerdo.
Título grande em azul-marinho (`#111827`), sans-serif negrito: **"Agentes de IA: quando a IA deixa de responder e passa a agir"**.
Subtítulo em cinza (`#4B5563`): "Definição, anatomia, tipos e aplicações — 2026".
Abaixo, uma faixa fina de destaque em azul (`#2563EB`) com uma frase: **"Um chatbot responde. Um agente decide, usa ferramentas e conclui a tarefa."**
Rodapé discreto com autor/organização e a data.
Estilo: moderno, minimalista, executivo.

---

## Slide 2 — Anatomia de um agente

**Mensagem-chave:** um agente é **um LLM + um harness** (tudo o que o cerca).

**Prompt de geração:**
Crie um slide explicativo com diagrama central em formato de "cérebro com extensões".
Fundo cinza muito claro (`#F7F8FA`).
Título em azul-marinho: **"Um agente é o modelo + tudo o que o cerca"**.
No centro, um círculo azul com o rótulo **"Modelo (LLM)"**. Ao redor, 5 caixas brancas com borda `#E5E7EB` e raio 16 px, ligadas ao centro por linhas finas:
- **Percepção** (ícone `globe`) — lê ambiente, entrada do usuário e resultados.
- **Planejamento** (ícone `target`) — decompõe o objetivo em passos.
- **Memória** (ícone `database`) — curto prazo (sessão) e longo prazo (fatos e histórico).
- **Ferramentas** (ícone `settings`) — APIs, busca, código, banco de dados.
- **Orquestração** (ícone `people`) — coordena passos, erros e limites.
Legenda central em cinza: "O modelo é a parte inteligente; o harness é tudo o resto."
Estilo: infográfico, clean, didático.

---

## Slide 3 — Como um agente pensa e age (o loop)

**Mensagem-chave:** o agente trabalha em **ciclo** — pensa, age, observa e repete até concluir.

**Prompt de geração:**
Crie um slide de processo com um fluxo circular e fechado.
Fundo branco.
Título em azul-marinho: **"O ciclo que define um agente"**.
Um loop de 4 etapas conectadas por setas curvas (ícone `arrow-right`):
1. **Pensar** (azul) — o modelo raciocina sobre o próximo passo.
2. **Agir** (azul escuro `#1D4ED8`) — chama uma ferramenta ou API.
3. **Observar** (verde `#16A34A`) — lê o resultado retornado.
4. **Repetir / Concluir** (amarelo `#D97706`) — ajusta e segue, ou entrega a resposta final.
Abaixo, duas linhas de rótulos: **ReAct** (raciocínio + ação) e **Plan-and-Execute** (planeja tudo e depois executa).
Legenda: "Dá para demonstrar em minutos; difícil é deixar confiável em produção."
Estilo: diagrama limpo, setas finas, sem excesso de detalhes.

---

## Slide 4 — Tipos de agentes

**Mensagem-chave:** os tipos diferem em **quanto planejam, o que lembram e como usam ferramentas**.

**Prompt de geração:**
Crie um slide de comparação em grade de 5 cards (2 em cima, 3 embaixo) com borda `#E5E7EB`, raio 16 px, fundo branco.
Fundo geral `#F7F8FA`.
Título em azul-marinho: **"Cinco tipos de agentes, da regra fixa à autonomia"**.
- **Reativo** (ícone `check`) — responde a regras fixas, baixa latência, sem estado.
- **Orientado a objetivo** (ícone `target`) — planeja múltiplos passos para atingir um fim.
- **Com ferramentas** (ícone `settings`) — chama APIs, buscadores e código.
- **Com memória** (ícone `database`) — mantém contexto entre interações (episódica, semântica, procedural).
- **Multiagente** (ícone `people`) — agentes especializados cooperam (planejador + executor + revisor).
Destaque em azul apenas no rótulo **"Multiagente"** (card mais avançado).
Legenda: "Os tipos não são exclusivos — um bom agente costuma ser híbrido."
Estilo: cards equilibrados, ícones outline, alinhamento perfeito.

---

## Slide 5 — Do uso à produção: aplicações e cuidados

**Mensagem-chave:** o valor vem de **casos com ROI claro** e de **guardrails** que tornem o agente confiável.

**Prompt de geração:**
Crie um slide de dois blocos lado a lado separados por uma linha vertical fina (`#E5E7EB`).
Fundo branco.
Título em azul-marinho: **"Onde os agentes já geram valor — e o que os mantém confiáveis"**.

Coluna esquerda — cabeçalho azul **"Onde aplicam"** (ícone `rocket`), com 4 itens curtos:
- Atendimento ao cliente (voz, chat e e-mail de ponta a ponta)
- Vendas e prospecção automatizadas
- Pesquisa de mercado e inteligência competitiva
- Análise de dados e conciliação de tarefas repetitivas

Coluna direita — cabeçalho amarelo `#D97706` **"O que exige cuidado"** (ícone `lock`), com 4 itens curtos:
- Permissões e superfície de risco das ferramentas
- Aprovação humana em decisões críticas (human-in-the-loop)
- Observabilidade e rastreamento do que o agente decidiu e por quê
- Avaliação contínua, custo e limites de execução

No rodapé, um KPI em azul: **"40%"** com legenda em cinza: "dos apps corporativos devem incluir agentes específicos de tarefa em 2026 (Gartner)".
Estilo: executivo, equilibrado, alto contraste, legível em projetor.

---

## Fontes consultadas (2026)

- IBM — *The 2026 Guide to AI Agents* / *What is a Multi-Agent System?*
- Redis — *AI Agent Architecture: Build Systems That Work in 2026*
- Firecrawl — *What Is AI Agent Architecture? Components and Patterns (2026)*
- MLflow — *Types of AI Agent Architectures: 2026 Developer Guide*
- JetBrains — *Types of AI Agents: A Complete Taxonomy for Developers*
- Red Hat — *Understanding AI agent types: a guide to categorizing complexity*
- CogitX — *AI Agents: Complete Overview (2026)*
