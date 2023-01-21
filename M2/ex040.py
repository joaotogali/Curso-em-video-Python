print('-='*20)
print('ESCOLA DO RIBAMAR')
print('-='*20)
nota1 = int(input('Primeira nota:'))
nota2 = int(input('Segunda nota:'))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')