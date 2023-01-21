dados = dict()
lista = list()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome:'))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['idade'] = int(input('Idade:'))
    soma += dados['idade']
    lista.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
#Até aqui foi a leitura dos dados
#Agora é o resultado
print('-='*30)
print(f'A) Ao todos temos {len(lista)} pessoas cadastradas')
media = soma/ len(lista)
print(f'B) A média de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}  ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')