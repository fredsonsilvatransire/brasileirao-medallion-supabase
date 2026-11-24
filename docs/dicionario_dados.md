# Dicionário de dados

Baseado em `dados/raw/Legenda.txt` + profiling realizado em 2026-11-24.

## Chaves e relacionamentos

- `partidas.ID` (único, 1–9165, sequencial) ⇄ `partida_id` nas demais tabelas.
- Nenhum órfão; nomes de clubes idênticos nas 4 tabelas (46 clubes, 15 UFs).

## campeonato-brasileiro-full.csv (partidas)

| Coluna | Tipo alvo | Observações |
|---|---|---|
| ID | int | PK |
| rodata | int | nome com typo → renomear `rodada` na Silver |
| data | date | formato `dd/mm/aaaa` |
| hora | time | `HH:MM` |
| mandante / visitante | text | |
| formacao_mandante / formacao_visitante | text | só a partir de 2014 |
| tecnico_mandante / tecnico_visitante | text | só a partir de 2014 |
| vencedor | text | `-` = empate (100% consistente com o placar) |
| arena | text | ~55% com `\xa0` no início → `strip` |
| mandante_Placar / visitante_Placar | int | |
| mandante_Estado / visitante_Estado | char(2) | UF |
| arrecadacao | numeric | só 2025 (valor bruto, R$) |

## campeonato-brasileiro-estatisticas-full.csv (clube × partida)

| Coluna | Tipo alvo | Observações |
|---|---|---|
| partida_id, rodata, clube | | sempre 2 linhas por partida |
| chutes, chutes_no_alvo, passes, faltas, cartao_amarelo, cartao_vermelho, impedimentos, escanteios | int | |
| posse_de_bola, precisao_passes | numeric | texto `"65%"` → número |

⚠️ Linhas totalmente zeradas = **dado ausente**, não zero: 2003–2014 e **2024 inteiro** (+ casos
pontuais em 2017, 2019, 2020). Converter para NULL na Silver.

## campeonato-brasileiro-gols.csv (gol)

| Coluna | Tipo alvo | Observações |
|---|---|---|
| partida_id, rodata, clube, atleta | | cobertura 2014–2025 |
| minuto | int + int | `"90+4"` → `minuto=90`, `acrescimo=4` |
| tipo_de_gol | text | vazio = normal; `Penalty`; `Gol Contra` |

Regra: em **Gol Contra**, `clube` é o time **beneficiado**. Soma de gols = placar em 100% das partidas.

## campeonato-brasileiro-cartoes.csv (cartão)

| Coluna | Tipo alvo | Observações |
|---|---|---|
| partida_id, rodata, clube, atleta | | cobertura 2014–**2024** (2025 ausente) |
| cartao | text | `Amarelo` / `Vermelho` |
| num_camisa | int | 1,8% nulo |
| posicao | text | 5,7% nulo; normalizar `Zagueira` → `Zagueiro` |
| minuto | int | |

362 registros clube×partida divergem da contagem de amarelos da tabela de estatísticas.

## Regras de negócio para a Silver

0. **Recorte**: somente temporadas >= 2014 (decisão de escopo). A Bronze mantém 2003–2025.
1. **Temporada ≠ ano civil**: temporada 2020 foi até fev/2021. Derivar `temporada` pela sequência de IDs/reinício de rodadas.
2. **Formato variável**: 2003–2004 (24 clubes, 46 rodadas), 2005 (22, 42), 2006+ (20, 38).
3. **2016** tem 379 jogos (Chapecoense × Atlético-MG não disputado).
4. Nomes de atletas sem padronização (nome completo vs. apelido) — risco para rankings.
