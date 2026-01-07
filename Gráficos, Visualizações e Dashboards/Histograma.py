# Criando Histograma com o Banco de Dados "Trees.csv"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leitura do dataset
base = pd.read_csv("trees.csv")

# Visualização inicial
print(base.head())

# Criação do histograma (array de frequências e classes)
h = np.histogram(base.iloc[:, 1], bins=6)
print(h)

# Visualização do histograma
plt.hist(base.iloc[:, 1], bins=6)
plt.title("Árvores")
plt.ylabel("Frequência")
plt.xlabel("Altura")
plt.show()
