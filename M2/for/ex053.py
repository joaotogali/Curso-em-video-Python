frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto [::-1]
#for letra in range(len(junto)-1,-1,-1):
    #inverso += junto[letra]
if inverso == junto:
    print('temos um palindromo')
else:
    print('nao temos um palindromo')