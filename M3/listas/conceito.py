#maipulando a lista
'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 4.')
print(num)
print(f'essa lista tem {len(num)} elementos')'''


#adicionando valores a uma lista vazia com append
'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)
valores.sort()

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

#Criando uma lista a partir do for
'''valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor:')))

for c, v in enumerate(valores):
        print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''


#situação de duas listas
a = [1, 2, 3, 4]
b = a[:]#aqui eu fatiei
b[2] = 9
print(f'Lista A:{a}')
print(f'Lista B:{b}')

