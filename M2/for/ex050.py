soma = 0
cont = 0
for c in range(1,7):
       num = int(input('Digite o {} valor:'.format(c)))
       if num % 2 == 0:
          cont += 1
          soma += num
print('Voce informou {} numeros pares e a soma deles é: {} '.format(cont,soma))