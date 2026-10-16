import pandas as pd

print('\n')

vendas = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4],
    'produto':    ['Notebook', 'Mouse', 'Teclado', 'Monitor']
})
print(vendas)
print('\n')

clientes = pd.DataFrame({
    'id_cliente': [1, 2, 3, 5],
    'nome':       ['Ana', 'Bruno', 'Carlos', 'Eva'],
    'cidade':     ['SP', 'RJ', 'MG', 'BA']
})
print(clientes)
print('\n')

resultado_merge = pd.merge(vendas, clientes, on='id_cliente')

print(resultado_merge)
print('\n')