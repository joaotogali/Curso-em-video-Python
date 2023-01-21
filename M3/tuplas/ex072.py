cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte' )
while True:
    num = int(input('Escolha um numero entre 0 e 20:'))
    if 0 <= num <= 20:
        break
    print('Tente novamente ')
print(f'Você escolheu o {cont[num]}')