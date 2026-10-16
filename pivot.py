import pandas as pd

dados = {
    'categoria': ['Eletrônicos', 'Eletrônicos', 'Eletrônicos', 'Eletrônicos',
                  'Roupas', 'Roupas', 'Roupas', 'Roupas',
                  'Alimentos', 'Alimentos', 'Alimentos', 'Alimentos'],
    'ano':       [2022, 2022, 2023, 2023,
                  2022, 2022, 2023, 2023,
                  2022, 2022, 2023, 2023],
    'vendas':    [1000, 1500, 2000, 2500,
                  800,  900,  1100, 1300,
                  500,  600,  700,  850]
}

df = pd.DataFrame(dados)

print('DataFrame Original')
print(df)
print('\n')

# aplicando pivit_table
tabela_pivot = df.pivot_table(
    index = 'categoria',
    columns = 'ano',
    values = 'vendas',
    aggfunc = 'sum'
)
print('vendas somadas por categoria e ano')
print(tabela_pivot)
print('\n')
