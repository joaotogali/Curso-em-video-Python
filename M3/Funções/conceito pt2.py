'''def contador(i, f, p):
   """
   -> Faz uma contagem e mostra na tela
   :param i: inicio da contagem
   :param f: fim da contagem
   :param p: passo da contagem
   :return: sem retorno
   """

   c = i
   while c <= f:
      print(f'{c} ', end='')
      c += p
   print('FIM!')


help(contador)
'''
#########################################################

'''Escopo de variaveis'
def funçao():
   n1 = 4
   print(f'N1 dentro vale {n1}')


n1 = 2
funçao()
print(f'N1 fora vale {n1}')'''
########################################################

'''def somar(a=0,b=0,c=0):
   s = a + b + c
   return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')'''
#################################################################
#Fazer o fatorial de um numero
'''def fatorial(num=1):
   f = 1
   for c in range(num, 0, -1):
      f *= c
   return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')'''
###################################################################

#Ver se o numero é par ou nao
def par(n=0):
   if n % 2 == 0:
      return True
   else:
      return False


num = int(input('Digite um numero:'))
if par(num):
   print('É par!')
else:
   print('Não é par!')