# Fazer um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa,
#retornando  um valor literal se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
def voto(num=0):
    atual = 2021
    idade = atual - num
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA "
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL "
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO "




num = int(input('Em que ano você nasceu?:'))
print(voto(num))
