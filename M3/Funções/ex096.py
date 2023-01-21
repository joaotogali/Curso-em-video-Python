
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
#  Ler a largura e comprimento e mostrar a área do terreno
def terr(l, c):
    area = l * c
    print(f'A área de um terreno {l}X{c} é de {area}m²')


print('Controle de Terrenos')
print('-='*15)

largura = float(input('LARGURA (m):'))
comprimento = float(input('COMPRIMENTO (m):'))

terr(largura,comprimento)