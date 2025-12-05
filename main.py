import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt

pd.set_option('display.precision', 3)


df = pd.read_csv('Data_Base.csv', sep=';')
notas = ["NU_NOTA_CH", "NU_NOTA_CN", "NU_NOTA_LC", "NU_NOTA_MT"]

print("\n=== Estatísticas das Notas ===")

# Média, mediana e moda usando *vetores inteiros*
grades_mean = df[notas].mean()
grades_median = df[notas].median()
grades_mode = df[notas].mode().iloc[0]   # retorna uma linha com a moda de cada coluna

print("Média das áreas:\n", grades_mean)
print("\nMediana das áreas:\n", grades_median)
print("\nModa das áreas:\n", grades_mode)

# Média geral dos participantes
df["MEDIA_GERAL"] = df[notas].mean(axis=1)

print(f"\nMédia geral dos participantes: {df['MEDIA_GERAL'].mean():.2f}")

# Distribuição completa de verificação
print("\n=== Frequência das Notas ===")
for col in notas:
    print(f"\nFrequências de {col}:")
    print(df[col].value_counts())

print("\n=== Distribuição das Idades ===")
print("Média:", df["NU_IDADE"].mean().round(2))
print("Mediana:", df["NU_IDADE"].median().round(2))
print("Moda:", df["NU_IDADE"].mode().iloc[0])

print("\n=== Quantidade de participantes por Estado ===")
print(df["SG_UF_PROVA"].value_counts())

print("\n=== Percentual de participantes por Estado (%) ===")
print((df["SG_UF_PROVA"].value_counts(normalize=True) * 100).round(2))

# === GRÁFICO ===

media_estados = df.groupby("SG_UF_PROVA")["MEDIA_GERAL"].mean().sort_values(ascending=False)

plt.figure(figsize=(12,6))
plt.bar(media_estados.index, media_estados.values)

plt.title("Estados com média geral mais alta do ENEM 2015")
plt.xlabel("Estado")
plt.ylabel("Média Geral")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('media_por_estado.png')
#plt.show()
