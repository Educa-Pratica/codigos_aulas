# Design System para Slides
## Moderno · Minimalista · Executivo · Tecnológico

> **Objetivo:** criar apresentações visualmente consistentes, claras e sofisticadas, com foco em narrativa, hierarquia da informação e tomada de decisão.

---

# 1. Princípios

## Clareza antes de decoração
Cada slide deve responder a uma pergunta ou transmitir **uma mensagem principal**.

## Hierarquia forte
O olhar deve encontrar, nesta ordem:

1. **Mensagem / insight**
2. **Evidência**
3. **Contexto**
4. **Detalhes**

## Espaço em branco é um componente
Não preencha todo o slide. O espaço vazio aumenta legibilidade e cria sofisticação.

## Consistência
Repita padrões de:

- tipografia;
- espaçamento;
- cores;
- ícones;
- cards;
- gráficos;
- alinhamento.

---

# 2. Canvas e Grid

## Formato

- **Proporção:** 16:9
- **Resolução recomendada:** 1920 × 1080 px

## Margens

| Elemento | Recomendação |
|---|---:|
| Margem lateral | 96 px |
| Margem superior | 72 px |
| Margem inferior | 72 px |
| Espaço entre blocos | 24–48 px |

## Grid

Utilize preferencialmente um grid de **12 colunas**.

**Regra:** elementos relacionados devem compartilhar alinhamentos horizontais ou verticais.

---

# 3. Paleta de Cores

## Base

| Token | Cor | Uso |
|---|---|---|
| `bg-primary` | `#FFFFFF` | Fundo principal |
| `bg-secondary` | `#F7F8FA` | Seções e áreas secundárias |
| `text-primary` | `#111827` | Títulos |
| `text-secondary` | `#4B5563` | Textos auxiliares |
| `border` | `#E5E7EB` | Bordas e divisórias |

## Destaques

| Token | Cor | Uso |
|---|---|---|
| `accent-primary` | `#2563EB` | Destaque principal |
| `accent-dark` | `#1D4ED8` | Contraste |
| `accent-soft` | `#DBEAFE` | Fundos suaves |
| `success` | `#16A34A` | Evolução positiva |
| `warning` | `#D97706` | Atenção |
| `danger` | `#DC2626` | Risco |

## Regra 70 / 20 / 10

- **70%:** fundos neutros e espaço vazio
- **20%:** texto e estrutura
- **10%:** cores de destaque

---

# 4. Tipografia

## Fonte principal

**Inter**

Alternativas:

- Aptos
- Manrope
- IBM Plex Sans
- Source Sans 3

## Escala

| Elemento | Tamanho |
|---|---:|
| Título de capa | 52–64 pt |
| Título do slide | 36–48 pt |
| Subtítulo | 22–28 pt |
| Texto | 18–24 pt |
| Legenda | 12–16 pt |
| KPI | 48–72 pt |

## Pesos

- **700:** títulos e números-chave
- **500–600:** subtítulos e labels
- **400:** texto corrido

### Regras

- Use no máximo **duas famílias tipográficas**
- Prefira alinhamento à esquerda
- Evite blocos longos
- Use negrito para transmitir significado

---

# 5. Espaçamento

Utilize uma escala baseada em múltiplos de 8.

| Token | Valor |
|---|---:|
| `space-1` | 8 px |
| `space-2` | 16 px |
| `space-3` | 24 px |
| `space-4` | 32 px |
| `space-5` | 40 px |
| `space-6` | 48 px |
| `space-8` | 64 px |

> Evite espaçamentos arbitrários.

---

# 6. Títulos

## Padrão recomendado

O título deve comunicar a **conclusão**, não apenas o assunto.

### ❌ Evite

**Resultados do Projeto**

### ✅ Prefira

**A automação reduziu o tempo operacional em 42%**

---

# 7. Cards

## Estrutura

```text
┌─────────────────────────────────┐
│  [ÍCONE]                        │
│                                 │
│  Título                         │
│  Descrição curta                │
│                                 │
│  Insight ou métrica             │
└─────────────────────────────────┘
```

## Especificação

- Fundo: branco
- Borda: `#E5E7EB`
- Border radius: **16 px**
- Padding: **24–32 px**
- Sombra: nenhuma ou extremamente sutil

### Regra

Evite colocar cards dentro de cards.

---

# 8. KPIs

## Estrutura

```text
42%
Redução no tempo operacional
```

### Regras

- número grande;
- descrição curta;
- contexto obrigatório;
- destaque visual controlado.

---

# 9. Ícones

Use os ícones do pacote fornecido com este Design System.

## Estilo

- outline;
- geometria simples;
- stroke consistente;
- sem sombras;
- sem gradientes;
- sem excesso de detalhes.

## Tamanhos

| Contexto | Tamanho |
|---|---:|
| Inline | 16–20 px |
| Card | 24–32 px |
| Destaque | 40–64 px |

### Regra de ouro

**Não misture estilos de ícones diferentes na mesma apresentação.**

---

# 10. Gráficos

## Princípios

- destaque apenas o dado importante;
- reduza elementos decorativos;
- remova grades desnecessárias;
- evite gráficos 3D;
- prefira rótulos diretos.

## Estratégia de cor

```text
████████████████████  Dado principal
██████               Contexto
████                 Contexto
```

Use a cor de destaque para **uma informação prioritária**. O restante deve permanecer neutro.

---

# 11. Estruturas de Slides

## 11.1 Capa

```text
TÍTULO PRINCIPAL

Subtítulo ou contexto


Autor / Organização                         Data
```

Características:

- muito espaço vazio;
- um elemento visual dominante, se necessário;
- poucos elementos.

---

## 11.2 Slide de Insight

```text
TÍTULO COM A PRINCIPAL CONCLUSÃO


EVIDÊNCIA / TEXTO          GRÁFICO / VISUAL
```

Ideal para apresentações executivas.

---

## 11.3 Três Pilares

```text
        01                02                03

       Ícone             Ícone             Ícone

       Pilar             Pilar             Pilar

     Descrição         Descrição         Descrição
```

Use apenas quando os três itens tiverem importância semelhante.

---

## 11.4 Processo

```text
[01] ─────→ [02] ─────→ [03] ─────→ [04]

Descobrir   Construir     Validar      Escalar
```

Evite diagramas excessivamente complexos.

---

## 11.5 Comparação

| | Atual | Futuro |
|---|---|---|
| Tempo | Alto | Reduzido |
| Automação | Baixa | Alta |
| Escalabilidade | Limitada | Elevada |

Destaque visualmente a coluna ou cenário desejado.

---

## 11.6 Roadmap

```text
Q1              Q2              Q3              Q4

●───────────────●───────────────●───────────────●

Discovery       MVP             Escala          Otimização
```

---

# 12. Imagens

## Recomendações

- prefira uma imagem forte a várias imagens pequenas;
- use imagens relevantes para a narrativa;
- evite imagens genéricas de banco;
- mantenha recortes consistentes.

## Tratamento

Quando necessário:

- overlay sutil;
- bordas arredondadas;
- alto contraste;
- composição limpa.

---

# 13. Animações

## Use apenas para

- revelar etapas;
- construir uma narrativa;
- direcionar atenção.

## Preferidas

- Fade
- Appear
- Morph
- Transições suaves

## Evite

- Bounce
- Spin
- Zoom agressivo
- Efeitos diferentes em cada slide

> A animação deve servir à narrativa, não chamar atenção para si mesma.

---

# 14. Acessibilidade

- Texto mínimo recomendado: **18 pt**
- Alto contraste entre texto e fundo
- Não comunicar significado apenas com cor
- Evitar textos sobre fundos visualmente complexos
- Garantir legibilidade em projetores

---

# 15. Checklist Final

## Mensagem

- [ ] Existe uma ideia principal?
- [ ] O título comunica um insight?
- [ ] Há informação desnecessária?

## Design

- [ ] Os elementos estão alinhados?
- [ ] Os espaçamentos são consistentes?
- [ ] A paleta está controlada?
- [ ] Os ícones possuem o mesmo estilo?

## Dados

- [ ] Os gráficos são legíveis?
- [ ] Métricas possuem contexto?
- [ ] A fonte dos dados está disponível?

---

# 16. Tokens

```css
:root {
  --bg-primary: #FFFFFF;
  --bg-secondary: #F7F8FA;

  --text-primary: #111827;
  --text-secondary: #4B5563;
  --border: #E5E7EB;

  --accent-primary: #2563EB;
  --accent-dark: #1D4ED8;
  --accent-soft: #DBEAFE;

  --success: #16A34A;
  --warning: #D97706;
  --danger: #DC2626;

  --radius-sm: 8px;
  --radius-md: 16px;
  --radius-lg: 24px;

  --space-1: 8px;
  --space-2: 16px;
  --space-3: 24px;
  --space-4: 32px;
  --space-5: 40px;
  --space-6: 48px;
  --space-8: 64px;
}
```

---

# 17. Regras de Ouro

1. **Uma ideia principal por slide**
2. **Títulos devem comunicar conclusões**
3. **Menos elementos, mais hierarquia**
4. **Espaço em branco é parte do layout**
5. **Destaque somente o que importa**
6. **Consistência supera criatividade aleatória**
7. **Dados sempre precisam de contexto**
8. **Se não adiciona significado, remova**

---

## Direção visual

**Moderno · Minimalista · Editorial · Executivo · Tecnológico**

A apresentação final deve transmitir:

> **clareza, confiança e domínio do conteúdo.**
