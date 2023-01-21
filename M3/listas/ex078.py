valores = list()
maior = 0
menor = 0
pos = -1
for cont in range(0,5):
    pos += 1
    valores.append(int(input(f'Digite um valor para a posição {pos}:')))

print('='*40)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi o {max(valores)} na posição {valores.index(max(valores))}...')
print(f'O menor valor digitado foi o {min(valores)} na posição {valores.index(min(valores))}...')



listanum = []
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end= ' ')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end= '')
print()
print(f'O menor valor digitado foi o {menor} na posição')
for i , v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()