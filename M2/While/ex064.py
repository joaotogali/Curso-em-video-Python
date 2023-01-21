num = soma = cont = 0
num = int(input('digite um valor[999 para parar]:'))
while num != 999:
        soma += num
        cont += 1
        num = int(input('digite um valor[999 para parar]:'))
print('você digitou {} numeros e a soma deles é {}'.format(cont, soma))

