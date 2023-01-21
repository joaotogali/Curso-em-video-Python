galera = list()
dado = list()
maior = menor = 0
while True:
    galera.append(str(input('Nome:')))
    galera.append(float(input('Peso:')))
    if len(dado) == 0:
        maior = menor = galera[1]
    else:
        if galera[1] > maior:
            maior = galera[1]
        if galera[1] < menor:
            menor = galera[1]

    dado.append(galera[:])#não esquecer de fatiar
    galera.clear()
    resp = str(input('Quer continuar: [S/N]'))
    if resp in 'Nn':
        break
print(f'Os dados foram {dado}')
print(f'Ao todo você cadastrou {len(dado)} pessoas')
print(f'O maior peso foi {maior}. Peso de ', end='')
for p in dado:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi {menor}', end='')
for p in dado:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
