import math
print('='* 20)
print('10 TERMOS DE UMA PA')
print('='* 20)
a1 = int(input('Digite o primeiro termo:'))
Razão = int(input('Digite a Razão:'))
cont = 1
termo = a1
total = 0
mais = 10
while cont != 0:
    total += mais
    while cont <= total:
        print('{} ->'.format(termo), end=' ')
        termo += Razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais:'))
print('Progressão finalizada com {} termos mostrados'.format(total))
