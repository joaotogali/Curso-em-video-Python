'''n = int(input('Informe a quantidade de linhas  da matriz A: '))
p = int(input('Informe a quantidade de colunas da matriz A: '))
A = []
for i in range(n):
    linha = []
    for j in range(p):
        val = int(input('Qual o valor do elemento da posição [' + str(i) + '][' + str(j) + '] da matriz A: '))
        linha.append(val)
    A.append(linha)
print(A)'''

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end= '')
    print()