def notas(*num, sit=False):
    """

    :param num: os valores das notas (podendo colocar quantas quiser)
    :param sit: a situação da média geral das notas, podendo ser 'BOA', 'RAZOÁVEL' e 'RUIM' (sendo opcional)
    :return: Mostrar todos os dados a partir de um dicionário
    """

    dados = dict()
    dados['total'] = len(num)
    dados['maior'] = max(num)
    dados['menor'] = min(num)
    dados['média'] = sum(num) / len(num)
    if sit:
        if dados['média'] >= 7:
            dados['situação'] = 'BOA'
        elif dados['média'] >= 5:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'RUIM'

    return dados


#programa principal
r = notas(1, 3, 6, 9, 2, sit=True)
print(r)
help(notas)