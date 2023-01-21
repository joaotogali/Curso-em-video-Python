print('-='*20)
print('BANCO DO BRASIL')
print('-='*20)
print('Seja bem vindo ao nosso sistema')
casa = int(input('Qual o valor da casa:'))
sal = int(input('Qual seu salário:'))
anos = int(input('Em quantos anos pretende pagar:'))
prestação = casa / (anos * 12)
minimo = sal * 0.30
print('Para pagar uma casa de R${} em {} anos, a prestação será de R${:.2f}'.format(casa,anos,prestação))
if prestação <= minimo:
    print('emprestimo pode ser concedido')
else:
    print('emprestimo negado')

