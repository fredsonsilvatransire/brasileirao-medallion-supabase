# ⚽ FutDados — Campeonato Brasileiro (2003–2025)

Projeto de engenharia e análise de dados sobre o Brasileirão Série A, construído sobre a
**arquitetura medalhão** (Bronze → Silver → Gold) no **Supabase**, com pipeline em **Python** e
dashboard em **HTML**.

> 🚧 Em construção.

**Escopo analítico:** temporadas **2014–2025**, período com cobertura de gols, cartões, técnicos e
formações. A Bronze guarda os CSVs completos (2003–2025), como cópia fiel da origem, e o recorte
é aplicado a partir da Silver.

**Dashboard:** HTML estático (GitHub Pages) que consulta a camada Gold **ao vivo** pela Data API
do Supabase, usando a chave pública `anon` e políticas RLS somente leitura.

## Arquitetura

```
CSV (dados/raw) ──► Bronze ──► Silver ──► Gold ──► Dashboard HTML (GitHub Pages)
                    bruto       tipado,     prontas
                    (texto) +   limpo,      para
                    metadados   modelado    análise
                    de carga
```

| Camada | Schema Supabase | Conteúdo |
|---|---|---|
| Bronze | `bronze` | Cópia fiel dos CSVs (todas as colunas como texto) + `_arquivo_origem`, `_carregado_em` |
| Silver | `silver` | Tipagem, limpeza, coluna `temporada`, dimensões e fatos |
| Gold | `gold` | Agregações consumidas pelo dashboard |

## Dados

| Arquivo | Linhas | Granularidade |
|---|---|---|
| `campeonato-brasileiro-full.csv` | 9.165 | partida |
| `campeonato-brasileiro-estatisticas-full.csv` | 18.330 | clube × partida |
| `campeonato-brasileiro-gols.csv` | 10.820 | gol |
| `campeonato-brasileiro-cartoes.csv` | 20.953 | cartão |

Detalhes, cobertura e regras de qualidade em [`docs/dicionario_dados.md`](docs/dicionario_dados.md).

**Fonte:** _a confirmar_ (provável: repositório/Kaggle "Campeonato Brasileiro de Futebol" de adaoduque).

## Estrutura

```
├── dados/raw/        # CSVs originais (imutáveis)
├── src/futdados/     # pipeline Python (bronze, silver, gold)
├── sql/              # DDL de schemas, tabelas e políticas RLS
├── tests/            # testes de qualidade de dados
├── dashboard/        # HTML/CSS/JS
└── docs/             # dicionário de dados e diagramas
```

## Como executar

```bash
uv sync                 # cria o ambiente e instala dependências
cp .env.example .env    # preencha as credenciais do Supabase
uv run pytest           # testes
```

## Stack

Python · pandas · Supabase (PostgreSQL) · HTML/CSS/JS · GitHub Actions · GitHub Pages

## Privacidade (LGPD)

O dataset contém nomes de atletas e técnicos (dados públicos de figuras públicas), utilizados
exclusivamente para fins estatísticos, sem cruzamento com outras bases de dados pessoais.
