num1 = int(input('Digite o valor de entrada:'))
num2 = int(input('Digite o valor final:'))

contador_pares = 0
while num1 <= num2:
    if num1 % 2 == 0 :
        contador_pares = contador_pares + 1
    num1 = num1 + 1
print(contador_pares)
