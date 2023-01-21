import math
dist = int(input('Qual a distância da sua viagem em Km:'))
if dist <= 200:
    valor1 = dist * 0.50
    print('Valor:R${}'.format(valor1))
else:
    valor2 = dist * 0.45
    print('Valor:R${}'.format(valor2))