# Criando um Boxplot com o Banco de Dados "Trees.csv" 

# Importação das bibliotecas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# caminho absoluto para o csv 
caminho_csv = r"C:\Users\laura\OneDrive\Área de Trabalho\Curso Python\Curso-Cientista-de-Dados-Estudo\Gráficos, Visualizações e Dashboards\trees.csv"

base = pd.read_csv(caminho_csv)

sns.set_style("whitegrid")
sns.boxplot(data=base, orient="h")
plt.title("Árvores")
plt.show()