#Deixar as linhas adaptadas ao texto

def escreva(msgn):
    tam = len(msgn) + 4
    print('~'* tam)
    print(f'  {msgn}')
    print('~' * tam)


escreva('Testando a função')
escreva('VASCO')
escreva('João Gabriel')