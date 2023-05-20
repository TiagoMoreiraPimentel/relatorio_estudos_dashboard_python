import pandas as pd
import matplotlib.pyplot as plt
import sys

# Lê o arquivo Excel
df = pd.read_excel("Organize 1.1.xlsx")

# Ordena o DataFrame pelo valor de "Despesa"
df = df.sort_values(by="Despesa", ascending=False)

# Cria o gráfico de colunas
plt.figure(figsize=(8,5)) # define o tamanho da janela
plt.bar(range(len(df)), df["Despesa"], width=0.4)
plt.xlabel("Descrição")
plt.ylabel("Despesa")
plt.title("Despesa por Data")
#plt.grid() # adiciona as linhas de marcação 'grade'

# Adiciona rótulos às barras
for i, v in enumerate(df["Despesa"]):
    plt.text(i, v, str(v), ha="center", va="bottom", fontweight="bold", fontsize=6, color="black", alpha=0.8)

# Define as posições dos rótulos no eixo x
plt.xticks(range(len(df)), df["Descricao"])

# Exibe o gráfico
plt.show()
