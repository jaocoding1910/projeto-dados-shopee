import pandas as pd

df = pd.read_csv("Dados/operacao_shopee.csv")


print("Primeiras linhas:")
print(df.head())

print("\nPedidos em Backlog:")
print(df[df["status"] == "Backlog"])

print("\nQuantidade por status:")
print(df["status"].value_counts())

total_pedidos = len(df)
backlog = (df["status"] == "Backlog").sum()

percent_backlog = (backlog / total_pedidos) * 100

print(f"\nPercentual de Backlog: {percent_backlog:.2f}%")
