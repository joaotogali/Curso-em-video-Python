altura = float(input('Digite sua altura: '))
peso = int(input('Digite seu peso: '))
calculo = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(calculo))
if calculo <18.5:
    print('abaixo do peso')
elif calculo >18.5 and 25:
    print('saudavel')
elif calculo >25 and 30:
    print('Peso em excesso')
elif calculo >30 and 35:
    print('Obesidade Grau I')
elif calculo >35 and 40:
    print('Obesidade Grau II')
elif calculo >=40:
    print('Obesidade Grau III')