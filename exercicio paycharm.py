import pandas as pd

data=pd.read_csv('kc_house_data.csv')
print(data.head())
print(data.shape)
print(data.columns)
print(data.sort_values('price'))
#questão 01) quantas casas estão disponiveis?Resposta: São de 21613
len(data['id'].unique())
# 02) Quantos atributos a casa tem? Resposta: 21 atributos
len(data.columns.tolist())
# 03) Quais são os atributo da casa?Resposta
data.drop(['id','date'],axis=1).columns.tolist