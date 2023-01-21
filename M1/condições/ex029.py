import math
print('--------------------------------')
print('        RADAR ELETRÔNICO        ')
print('--------------------------------')
vel = int
vel_permitida = 80
vel_atual = int(input('Qual velocidade seu carro estava:'))
if vel_atual > 80:
    print('MULTADO')
    multa = (vel_atual - 80) * 7
    print('VALOR:R${}'.format(multa))

else:
    print('VELOCIDADE PERMITIDA')
