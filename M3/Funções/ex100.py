'''Fazer um programa que tenha uma lista chamada sorteio() e somapar(). A primeira função vai sortear 5 numeros e vai coloca-los
 dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.'''
from random import randint
from time import sleep

def sorteio(sort):

    print(f'Sorteando 5 valores da lista: ', end='')
    for i in range(0,5):
        num = randint(1,10)
        sort.append(num)
        print(f' {num} ', end='', flush= True)
        sleep(0.5)
    print('PRONTO!')

def somaPar(sort):
    s = 0
    for valor in sort:
        if valor % 2 == 0:
            s += valor
    print(f'Somando os valores pares de {sort}, temos {s}')



#programa principal
numeros = list()
sorteio(numeros)
somaPar(numeros)
