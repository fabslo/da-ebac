import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('gasolina.csv')
sns.set(style='whitegrid')

sns.lineplot(x='dia', y='venda', data=dados)

plt.ylabel('Venda')
plt.xlabel('Dia')
plt.title('Variação do Preço da Gasolina ao Longo Dos Dias')
plt.savefig('gasolina.png')

plt.show()