'''def lin():
    print('-='*30)

lin()
print('   João Gabriel    ')
print('     18 anos       ')
print('    Sistemas de informação    ')
lin()'''
###################################################
'''def titulo(txt):
    print('-'*30)
    print(txt)
    print('-' * 30)


titulo(' Curso em video')
titulo(' Python é muito bom')'''
###################################################
#Exemplos

'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B é igual a {s}')

#Programa principal
soma(b=3,a=6)
soma(1,2)
soma(2,2)'''
###################################################
'''def contador(*num):
    #for valor in num:
       #print(f'{valor} ', end='')
    #print('FIM!')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros ')


contador(2, 1, 4, 5)
contador(9, 0, 6)
contador(7, 5, 6)'''
###################################################
'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [3, 5, 6, 8]
dobra(valores)
print(valores)'''

def soma( * valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5,7)
soma(8,9,7)
