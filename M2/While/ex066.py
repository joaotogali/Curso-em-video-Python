num = soma = 0
while True:
    num = int(input('digite um valor[999 para parar]:'))
    if num == 999:
        break
    soma += num
print(f'A soma dos valores é {soma}')

