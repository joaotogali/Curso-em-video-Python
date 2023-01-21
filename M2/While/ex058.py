from random import randint
num = int(randint(0,11))
print('Olá sou seu computaor...')
print('Acabei de pensar em um numero de 0 a 10')
palpite = int(input('Palpite:'))
cont = 1
while num != palpite :
        palpite = int(int(input('tente denovo:')))
        cont += 1
else:
    print('Acertou com {} tentativas, Parabéns!'.format(cont))

