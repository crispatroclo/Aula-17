import pandas as pd

df = pd.read_csv(r"C:\Users\cristiane.patroclo\Downloads\funcionarios.csv")

#print(df)
#print('\n')

#print(df.columns) # nomes das colunas
#print('\n')

#print(df.index) # Índices 
#print('\n')

#print(df.values) # indices
#print('\n')

#print(df.info()) # tipos, valores nulos, memória     
#print('\n')

# extrair a media dos salarios de cada departamento usando o groupby
#print(df.groupby('departamento')['salario'].mean())
#print('\n')

#print(df.groupby('departamento').agg(media_salario = ('salario', 'mean')))
#print('\n')

#print(df.groupby('departamento').agg({'salario':['mean']}))
#print('\n')

# anterior comprint com numero formatado
#print(df.groupby('departamento')['salario'].mean().round(2))
#print(df.groupby('departamento')['salario'].mean().map('{:5.2f}'.format))
#print('\n')


# agrupar por mais de um categoria: departamento e situação de funcionario
#print(df.groupby(['departamento', 'ativo']).size())
#print('\n')

#print(pd.crosstab(df['departamento'], df['ativo']))
#print('\n')


# agrupar por departamento e agregação de carias colunas
#print(df.groupby('departamento').agg(
#    quantidade_funcionarios=('id', 'count'),
#    salario_medio = ('salario','mean'),
#    maior_salario = ('salario', 'max'),
#    lucro_total = ('lucro', 'sum')
#).round(2))        

#print(df.groupby('departamento').agg(
#    quantidade_funcionarios=('id', 'count'),
#    salario_medio = ('salario','mean'),
#    maior_salario = ('salario', 'max'),
#    lucro_total = ('lucro', 'sum'),
#).round(2)) 

#tabela_pivot_sum = df.pivot_table(
#    index = 'departamento', # define a coluna que será usada como linha da tabela
#    columns = 'ativo', # define a coluna que será usada como coluna
#    values = 'salario', # 
#    aggfunc = 'sum'   
#)
#print('tabela_pivot_sum')
#print(tabela_pivot_sum)
#print('\n')

#tabela_pivot_mean = df.pivot_table(
#    index = 'departamento', # define a coluna que será usada como linha da tabela
#    columns = 'ativo', # define a coluna que será usada como coluna
#    values = 'salario', # 
#    aggfunc = 'mean'   
#)
#print('tabela_pivot_mean')
#print(tabela_pivot_mean)
#print('\n')

#df = df.sort_values('salario') # organiza o dataframe pelos valores da coluna salario de dorma crescente
#print(df)
#print('\n')

#df = df.sort_values('salario', ascending=False) # organiza o dataframe pelos valores da coluna salario de ordem descrescente
#print(df)

df = df.sort_values(['salario', 'lucro'])
print(df)
print('\n')

df = df.sort_values(['lucro', 'salario'])
print(df)
print('\n')