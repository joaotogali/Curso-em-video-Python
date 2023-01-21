#Fazer um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# O programa tem que analisar todos e dizer qual é o maior.
'''from time import sleep
def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram encontrados {cont} valores ao todo')
    print(f'O maior valor é o {maior}')


#programa principal
maior(2, 5, 6)
maior(2, 7, 5)'''

#Fazer um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# O programa tem que analisar todos e dizer qual é o maior.
from time import sleep
def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores...')
    for valor in num:
        print(f'{valor} ', end='')

        if valor == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram encontrados {cont} valores ao todo.')
    print(f'O maior valor informado foi o {maior}')


#programa principal
maior(9, 8, 4)
maior(8, 4, 9, 5)
maior(6, 7, 8)