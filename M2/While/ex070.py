p = 0
cont = 0
total = 0
soma = 0
maior = 0
menor = 0
barato = ' '
while True:
    nome = str(input('Nome do produto:'))
    p = float(input('Preço:R$'))
    total += p

    escolha = ' '
    while escolha not in "SN":
        escolha = str(input('Quer continuar:[S/N]')).strip().upper()[0]
        if p > 1000:
            cont += 1
        if cont == 1 or p < menor:
            menor = p
            barato = nome
      

    if escolha == 'N':
        break
print('------Fim do programa------')
print(f'O total da compra foi {total}')
print(f'Temos {cont} produtos acima de R$1000.00')
print(f'O produto mais barato é o {barato} e custa {menor}')