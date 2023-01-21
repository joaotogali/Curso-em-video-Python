def ficha(j ='<desconhecido>', gols=0 ):
    print(f'O jogador {j} fez {gols} gols no campeonato')


#programa principal
n = str(input('Nome do jogador:'))
g = str(input('Quantos gols o jogador fez:'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
