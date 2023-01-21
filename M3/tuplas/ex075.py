num = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')))
print(f'Você digitou os numeros {num}')
print(f'O valor 4 apareceu {num.count(4)} vezes')
if 3 in num:
    print(f'O primeiro valor 3 foi digitado na {num.index(3)+1}° posição')
else:
    print('O Valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
