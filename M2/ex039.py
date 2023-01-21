print('-='*20)
print('ALISTAMENTO MILITAR')
print('-='*20)
idade = int(input('Digite sua idade:'))
if idade < 18 :
    print('AINDA VAI SE ALISTAR')
    tempo = 18 - idade
    print('FALTAM {} ANOS '.format(tempo))
elif idade == 18:
    print('HORA DE SE ALISTAR')
elif idade > 18:
    print('PASSOU DO TEMPO')
    tempo = idade - 18
    print('JA PASSOU {} ANOS '.format(tempo))

