nome = str(input('Digite seu nome:')).lower()
if nome == 'joao':
    print('Que nome bonito!')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('seu nome é bem popular no brasil!')
elif nome in ('Ana claudia jessica isabella'):
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal .-.')

print('Tenha um bom dia {}!'.format(nome))

