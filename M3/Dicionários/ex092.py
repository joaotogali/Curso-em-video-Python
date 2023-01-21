dados = dict()
#Ler os dados
while True:
    nome = str(input('Nome:'))
    dados['nome'] = nome
    ano_nasc = int(input('Ano de Nascimento:'))
    dados['nascimento'] = ano_nasc
    carteira_trabalho = int(input('Carteira de trabalho (0 se não tem):'))
    dados['ctps'] = carteira_trabalho
    if carteira_trabalho == 0:
      print('-=' * 30)
      print(f'nome é igual a {nome}')
      print(f'não possui carteira de trabalho')
      break
    else:
        if carteira_trabalho != 0:
            contr = int(input('Ano de contratação:'))
            dados['contratação'] = contr
            salario = int(input('Salário: R$'))
            dados['salario'] = salario
            print('-='*30)
            for k, v in dados.items():
                print(f'  -{k} tem o valor de {v}')
            apos = contr + 32
            dados['aposentadoria'] = apos
            for i in range(1):
                print(f'  -{dados["nome"]} se aposenta em {apos}')
    break
print('-='*30)