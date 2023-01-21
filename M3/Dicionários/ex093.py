from random import randint

dados = dict()
partidas = list()
nome = str(input('Nome:'))
dados['nome'] = nome
total = int(input(f'Quantas partidas {dados["nome"]} jogou?:'))
for i in range(0, total):
    partidas.append(int(input(f' Quantos gols da partida{i}?')))
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas')
for j, v in enumerate(dados['gols']):
    print(f'         => Na partida {j} fez {v} gols')
print(f'Foi um total de {dados["total"]} gols')