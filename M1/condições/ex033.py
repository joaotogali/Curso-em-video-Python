a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
#verificação de menor valor
menor = a
soma = a + b + c
if b<a and b <c:
    menor = b
elif c<a and c<b:
    menor = c

#verificação de maior valor
elif b>a and b>c:
    maior = b
elif c>a and c>b:
    maior = c

#verificação do produto
elif b * a * c:
    multi = a * b * c
    print(multi)

#verificação de soma
elif  a + b + c:
    soma = a + b + c


print('O menor valor verificado foi o {}'.format(menor))
print('o maior valor verificado foi o {}'.format(maior))
print('O produto entre os numeros é {}'.format(multi))