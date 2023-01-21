print('Tabela de multiplicação de 1 a 10')
for x in range (1,11):
    for y in range  (1,11):
        mult = x * y
        print('{} x {} = '.format(x, y), mult)