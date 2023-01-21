listagem = ('Láspis', 1.75,
            'Borracha', 2,
            'Apontador', 3.50,
            'Estojo', 20,
            'Mochila', 100,
            'Livro', 34.50,
            'Compasso', 10
            )
print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end='')
    else:
        print(f'f{listagem[pos]:>7.2f}')
print('-'*40)