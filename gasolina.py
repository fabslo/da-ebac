import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('gasolina.csv')
sns.set(style='whitegrid')

sns.lineplot(x='dia', y='venda', data=dados)

plt.ylabel('Preço')
plt.xlabel('Dia')
plt.title('Variação do Preço ao Longo Dos Dias \n Teste para mostrar uma diferença no branch')
plt.savefig('gasolina.png')

plt.show()