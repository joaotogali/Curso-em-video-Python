r = 'S'
soma = qnt = media = maior = menor = 0
while r in 'Ss':
    num = int(input('Digite um número:'))
    soma += num
    qnt += 1
    if qnt == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input('Quer continuar? [S/N]:')).lower().strip()[0]
media = soma / qnt
print('Você digitou {} numeros e a media foi {}'.format(qnt, media))
print('O maior numero é o {} e o menor numero é o {}'.format(maior,menor))