
import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'nome': ['Ana', 'Bruno', 'Carlos'],
    'idade': [25, 30, 35]
})
#print(df1)
#print('\n')

df2 = pd.DataFrame({
    'id': [4, 5, 6],
    'nome': ['Diana', 'Eduardo', 'Fernanda'],
    'idade': [28, 32, 40]
})
#print(df2)
#print('\n')

df_notas = pd.DataFrame({
    'matematica': [8.5, 7.0, 9.0],
    'portugues':  [7.5, 8.0, 6.5]
})
#print(df_notas)
#print('\n')

resultado_vertical = pd.concat([df1, df2])
print(resultado_vertical)
print('\n')

resultado_horizontal = pd.concat([df1, df_notas], axis=1)
print(resultado_horizontal)
print('\n')