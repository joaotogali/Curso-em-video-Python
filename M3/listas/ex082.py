valores = list()
valores2 = list()
valores3 = list()
resp = ' '
while True:
    valores.append(int(input('Digite um valor:')))
    resp = str(input('Deseja continuar?: [S/N]')).upper()

    if resp in 'N':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        valores2.append(v)
    elif v % 2 == 1:
        valores3.append(v)

print(f'A lista completa é {valores}')
print(f'a lista de pares é {valores2}')
print(f'A lista de impares é {valores3}')