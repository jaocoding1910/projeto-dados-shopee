import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / "Dados" / "operacao_shopee.csv"
db_path = BASE_DIR / "Dados" / "operacao_shopee.db"

# Carrega CSV
df = pd.read_csv(csv_path)

# Cria banco e tabela
conn = sqlite3.connect(db_path)
df.to_sql("operacao_shopee", conn, if_exists="replace", index=False)

# Consultas SQL reais
queries = {
    "Status count": """
        SELECT status, COUNT(*) AS quantidade
        FROM operacao_shopee
        GROUP BY status;
    """,
    "Backlog orders": """
        SELECT pedido_id, status, data_recebimento
        FROM operacao_shopee
        WHERE status = 'Backlog'
        ORDER BY data_recebimento;
    """
}

for name, q in queries.items():
    print(f"\n--- {name} ---")
    print(pd.read_sql_query(q, conn))

conn.close()
print("\n✅ SQLite database created at:", db_path)
