import pandas as pd

df = pd.DataFrame({
    'categoria': ['A', 'B', 'A', 'B', 'A'],
    'vendas': [100, 200, 150, 300, 120],
    'quantidade': [1, 2, 1, 3, 2]
})

print(df)

# Média de vendas por categoria
print(df.groupby('categoria')['vendas'].mean())

#print(df)
#print("\n")

# Soma por categoria (todas as colunas numéricas)
#df.groupby('categoria').sum()

#print(df.groupby('categoria').sum())

# Agrupar por multiplas colunas
#df.groupby(['categoria', 'quantidade'])['vendas'].sum()

#print(df.groupby(['categoria', 'quantidade'])['vendas'].sum())

#Todas as operações na coluna vendas agrupadas pela coluna categoria
#df.groupby('categoria')['vendas'].agg(['sum', 'mean', 'max', 'count'])

#print(df.groupby('categoria')['vendas'].agg(['sum', 'mean', 'max', 'count']))

# Ou com nomes personalizados
#print(df.groupby('categoria').agg(
#   total_vendas=('vendas', 'sum'),
#    media_vendas=('vendas', 'mean'),
#    qtd_registros=('vendas', 'count')
#))

print(df.groupby('categoria')['vendas'].min)
print('\n')
print(df.groupby('categoria')['vendas'].max)
