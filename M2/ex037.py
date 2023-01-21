num = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para Binario
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('Sua opção:'))
if opção ==1:
    print('{} convertido para binario é igual á {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('{} ocnvertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertidp para hexadecimal é igual a {}'.format(num,hex(num)[2:]))
else:
    print('opção invalida, tente novamente')