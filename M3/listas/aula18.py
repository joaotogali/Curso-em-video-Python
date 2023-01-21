'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])#Não esquecr de fatiar
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])#Não esquecr de fatiar
print(galera)'''


'''galera = [['João', 18], ['Pedro', 15], ['Francisco', 32], ['Maria', 17]]
#print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''




galera = list()
dado = list()
totmai = totmen = 0

for c in range(0,3):
    dado.append(str(input('Nome:')))
    dado.append(str(input('Idade:')))
    galera.append(dado[:])#não esquecer de fatiar
    dado.clear()

for p in galera:
    if p[1] >= str(21):
        print(f'{p[0]} é menor de idade')
        totmen += 1
    else:
        print(f'{p[0]} é maior de idade')
        totmai += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')