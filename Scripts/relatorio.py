import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "Dados" / "operacao_shopee.csv"
REPORTS_DIR = BASE_DIR / "Reports"
REPORTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(CSV_PATH)
df["data_recebimento"] = pd.to_datetime(df["data_recebimento"])

# KPIs
total = len(df)
backlog = int((df["status"] == "Backlog").sum())
packed = int((df["status"] == "Packed").sum())
outbounded = int((df["status"] == "Outbounded").sum())
pct_backlog = (backlog / total * 100) if total else 0

# Resumo por dia
daily = (df.groupby(df["data_recebimento"].dt.date)["pedido_id"]
           .count()
           .reset_index(name="orders"))

# Gráfico 1: status
counts = df["status"].value_counts()
plt.figure()
plt.bar(counts.index, counts.values)
plt.title("Orders by Status")
plt.xlabel("Status")
plt.ylabel("Count")
chart_status = REPORTS_DIR / "status_distribution.png"
plt.savefig(chart_status, bbox_inches="tight")
plt.close()

# Gráfico 2: trend diário
plt.figure()
plt.plot(daily["data_recebimento"], daily["orders"], marker="o")
plt.title("Orders per Day")
plt.xlabel("Date")
plt.ylabel("Orders")
plt.xticks(rotation=25)
chart_daily = REPORTS_DIR / "daily_trend.png"
plt.savefig(chart_daily, bbox_inches="tight")
plt.close()

# Salvar KPI summary em CSV
summary = pd.DataFrame([{
    "total_orders": total,
    "backlog": backlog,
    "packed": packed,
    "outbounded": outbounded,
    "backlog_pct": round(pct_backlog, 2)
}])
summary_path = REPORTS_DIR / "kpi_summary.csv"
summary.to_csv(summary_path, index=False)

print("✅ Report generated:")
print("-", chart_status)
print("-", chart_daily)
print("-", summary_path)
