# Exercício Faça Você Mesmo

# Carregar Bibliotecas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ler o arquivo no meu armazenamento 
caminho_csv = r"C:\Users\laura\OneDrive\Área de Trabalho\Curso Python\Curso-Cientista-de-Dados-Estudo\Gráficos, Visualizações e Dashboards\dados.csv"

base = pd.read_csv(caminho_csv, sep=";")

# Visualização inicial
print(base.head())
# Saber quantas linhas e colunas
base.shape
base.info()
base.isnull().sum()
base.describe()

#Analisando o PIB
base['PIB'].median()
base['PIB'].describe()
# A média do PIB dos municípios analisados é de aproximadamente 19808, enquanto a mediana é 17206, indicando uma distribuição assimétrica influenciada por municípios com PIB elevado.

#Analisando VALOREMPENHO
base['VALOREMPENHO'].median()
base['VALOREMPENHO'].describe()

# PIB x VALOREMPENHO
base[['PIB', 'VALOREMPENHO']].corr()

# Criando a Visualização do Gráfico de Dispersão
sns.scatterplot(
    x=base['PIB'],
    y=base['VALOREMPENHO']
)

plt.title('Relação entre PIB e Valor Empenhado')
plt.xlabel('PIB do Município')
plt.ylabel('Valor Empenhado')

plt.show()
