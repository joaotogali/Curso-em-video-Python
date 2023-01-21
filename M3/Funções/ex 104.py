def leiaInt(resp):
        i = False
        v = 0
        while True:
                n = str(input(resp))
                if n.isnumeric():
                        v = int(n)
                        i = True
                else:
                     print('\033[0:31mERRO!44Digite um número inteiro válido.\033[m')
                if i:
                     break
        return v


#programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')