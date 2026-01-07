"""
Seção 10 – Introdução à Limpeza de Dados
"""
import pandas as pd
import statistics as sts

# Leitura do dataset
dataset = pd.read_csv("tempo.csv", sep=";")

print("Dataset original:")
print(dataset.head())

print("\nInformações do dataset:")
print(dataset.info())

# Tratamento da Umidade (mediana)
mediana_umidade = sts.median(dataset["Umidade"].dropna())
dataset["Umidade"] = dataset["Umidade"].fillna(mediana_umidade)

# Tratamento da coluna Vento (moda)
moda_vento = dataset["Vento"].mode()[0]
dataset["Vento"] = dataset["Vento"].fillna(moda_vento)

# Validação final
print("\nValores ausentes após limpeza:")
print(dataset.isnull().sum())

print("\nDataset final após limpeza:")
print(dataset)
