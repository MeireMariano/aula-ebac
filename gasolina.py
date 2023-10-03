# código de geração do gráfico
from pandas.core.groupby import groupby
# importando as bibliotecas
import csv
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# fazendo a leitura do arquivo csv
data = pd.read_csv('gasolina.csv')

# gerando um DataFrame
df = pd.DataFrame(data)

# código para gerar o gráfico
with sns.axes_style('whitegrid'):
  grafico=sns.lineplot(data=df,x="dia",y="venda",palette="pastel")
  grafico.set(title='Preço da gasolina por dia',xlabel='Dia',ylabel='Valor')

plt.savefig('gasolina.png')
plt.show()