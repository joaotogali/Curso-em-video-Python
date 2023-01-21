#Fazer uma função chamada contador(), que receba três parâmetros: 'inicio', 'fim' e 'passo' e realize a contagem
#O programa tem que realizar 3 contagens atráves da função criada:
# A) de 1 até 10, de 1 em 1
# B) de 10 a 0, de 2 em 2
# Uma contagem personalizada

# Exercicio resolvido
#A)
from time import sleep

def contador(inicio, fim, passo):

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}', )
    sleep(2.5)

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush= True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush= True)
            sleep(0.5)
            cont -= passo
        print('FIM!')


#Programa principal

contador(1, 10, 1)
contador(10,0,2)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('passo:'))
contador(i, f, p)


#######################################################################

from time import sleep


def contador(x, y, z):
    if z < 0:
        z *= -1
    if z == 0:
        z = 1
    print('-=-' * 15)
    print(f'Contagem de {x} até {y} de {z} em {z}')
    sleep(2)

    if x < y:
        for c in range(x, y+1, z):
            print(c, end=' ')
            sleep(0.5)
        print()

    else:
        for c in range(x, y-1, -z):
            print(c, end=' ')
            sleep(0.5)
        print()

# principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=-' * 15)
print('Agora é a sua vez de contar: ')
x = int(input('INICIO: '))
y = int(input('FIM:    '))
z = int(input('PASSO:  '))
contador(x, y, z)