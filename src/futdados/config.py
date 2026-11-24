"""Configurações centrais do projeto: caminhos e variáveis de ambiente."""

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT_DIR / "dados" / "raw"

load_dotenv(ROOT_DIR / ".env")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_DB_URL = os.getenv("SUPABASE_DB_URL")

RAW_FILES = {
    "partidas": RAW_DIR / "campeonato-brasileiro-full.csv",
    "estatisticas": RAW_DIR / "campeonato-brasileiro-estatisticas-full.csv",
    "gols": RAW_DIR / "campeonato-brasileiro-gols.csv",
    "cartoes": RAW_DIR / "campeonato-brasileiro-cartoes.csv",
}
