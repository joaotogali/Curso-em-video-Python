print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
   print('Os elementos podem formar um triângulo', end='')
   if r1 == r2 == r3:
    print('Equilátero')
   elif r1 != r2 != r3 != r1:
    print('Escaleno')
   else:
    print('Isoceles')
else:
    print('Nao podem formar um triangulo')

