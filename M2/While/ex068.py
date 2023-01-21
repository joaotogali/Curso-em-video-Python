from random import randint
print('-'*30)
print('VAMOS JOGAR ÍMPAR OU PAR')
print('-'*30)
v = 0
while True:
     num = int(input('Digite um valor:'))
     computador = randint(0,10)
     total = num + computador
     tipo = ' '
     while tipo not in 'PI':
         tipo = str(input('Par ou Ìmpar:[P/I]')).strip().upper()
     print(f'você jogou {num} e o computador jogou {computador} e a soma foi {total}')
     if tipo == 'P':
         if total % 2 == 0:
             print('Você ganhou')
             v += 1
         else:
             print('Você perdeu')
             print('GAME OVER')
             break
     if tipo == 'I':
         if total % 2 == 0:
             print('Você perdeu')
             print('GAME OVER')
         else:
             print('Você ganhou')
             v += 1

print(f'Você venceu {v} vezes')
