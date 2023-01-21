r = str(input('Qual é o seu sexo[M/F]:')).upper().strip()[0]
while r not in 'MF':
        r = str(input('Dados invalidos, por favor informe seu sexo [M/F]:'))
print('Sexo {} registrado com sucesso'.format(r))