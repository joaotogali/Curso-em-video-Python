v1 = int(input('Primeiro valor:'))
v2 = int(input('Segundo valor:'))
soma = v1 + v2
mult = v1 * v2
maior = 0
opção = 0
while opção != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior 
[ 4 ] novos números
[ 5 ] sair do programa''')
opção = int(input('Qual a sua opção:'))
if opção == 1:
    soma = v1 + v2
    print(soma)
elif opção == 2:
    print(mult)
while opção == 3:
    if v1 > v2:
        maior = v1
        print('O maior é o {}'.format(maior))
    elif v2 > v1:
        maior = v2
        print('O maior é o {}'.format(maior))
while opção == 4:
    opção = int(input('Qual a sua opção:'))
if opção == 5:
    print('Fim')






