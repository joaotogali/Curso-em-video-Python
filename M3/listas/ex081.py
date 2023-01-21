valores = list()
resp = ' '
while True:
    n = (int(input('Digite um valor:')))
    if n not in valores:
        valores.append(n)
    resp = str(input('Deseja continuar?: [S/N]')).upper()
    if resp in 'S':
        print('Valor adicionado com sucesso...')
    else:
        break

print(f'essa lista tem {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista...')

