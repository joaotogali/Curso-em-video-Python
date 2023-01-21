print('-='*20)
print('CONFERDERAÇÃO NACIONAL DE NATAÇÃO')
print('-='*20)
ano_nasc = int(input('Digite o ano em que o atleta nasceu:'))
ano_atual = 2021
idade = ano_atual - ano_nasc
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade > 19 and idade <= 20:
    print('SÊNIOR')
elif idade > 20:
    print('MASTER')

