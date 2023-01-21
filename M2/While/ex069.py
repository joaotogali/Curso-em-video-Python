idade = 0
mais18 = 0
cont = 0
ir = ' '
sexo = ' '
tothomem = 0
totmulher20 = 0
while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)
    print('              ')
    idade = int(input('Idade:'))
    sexo = str(input('Sexo:[M/F]')).lower().strip()[0]
    print('-' * 30)
    ir = str(input('Quer continuar:[S/N]'))
    print('              ')
    if idade > 18:
        cont += 1

    if sexo in 'm':
        tothomem += 1

    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

    if ir in 'Nn':
        break

print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {tothomem} homem cadastrado')
print(f'Total de mulheres com menos de 20 anos: {totmulher20}')



