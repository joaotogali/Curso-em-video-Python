#fazer uma analise de dados
#idade média
#mais jovem
#mais velha
#homem mais velho
#mulher mais velha
#############################################################

soma = 0
media = 0
velho = 0
jovem = 0
pessoavelha = 0
pessoanova = 0
mais_Velho = ''
mais_Jovem = ''
nomeHomemMais_Velho = ''
nomeMulherMais_Jovem = ''

for a in range(1, 4):

    nome = input('Digite o seu nome: ')
    sexo = input('Masculino ou Feminino ? [M/F]').upper()[0]
    idade = int(input('Digite a sua idade : '))
    print('-' * 20)

    soma = soma + idade
    media = soma / a

    if sexo == 'M' and idade >= velho:
        velho = idade
        nomeHomemMais_Velho = nome

    if sexo == 'F' and idade > jovem:
        jovem = idade
        nomeMulherMais_Jovem = nome

    if sexo in 'M or F' and idade > pessoavelha:
        pessoavelha = idade
        mais_Velho = nome

    if sexo in 'M or F' and idade <= pessoanova:
        pessoanova = idade
        mais_Jovem = nome

print('Media das idades é de {:.2f} '.format(media))
print('Nome do homem mais velho é {}'.format(nomeHomemMais_Velho))
print('Nome da mulher mais jovem é {}'.format(nomeMulherMais_Jovem))
print('A pessoa mais velha é {}'.format(mais_Velho))
print('A pessoa mais nova é {}'.format(mais_Jovem))