
aluno = dict()
#Ler nome e média
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'média de {aluno["nome"]}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
#restrições
else:
    aluno['situação'] = 'Reprovado'
#Mostre o conteúdo da estrutura de cada aluno
for k, v in aluno.items():
    print(f'{k} é igual a {v}')