from random import randint
from time import sleep
from operator import itemgetter
jogo = { 'jogador1': randint(1,5),
        'jogador2': randint(1,5),
        'jogador3': randint(1,5),
        'jogador4': randint(1,5)}

ranking = list()
print('Valores sorteados: ')

for k, v in jogo.items():
        print(f'{k} tirou {v} no dado')
        sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse= True )
print('-='*15)
print('==RANKING==')
for i, v in enumerate(ranking):
        print(f'{i+1}° lugar: {v[0]} com {v[1]}')
        sleep(1)