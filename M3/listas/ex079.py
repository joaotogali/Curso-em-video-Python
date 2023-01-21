valores = list()
resp = ' '
while True:
    n = (int(input('Digite um valor:')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado...')

    resp = str(input('Deseja continuar?: [S/N]')).upper()

    if resp in 'Nn':
        break

valores.sort()
print(f'Você digitou os valores {valores}')