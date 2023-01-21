def fatorial(n, show=False):
    """

    :param n: O numero calculado
    :param show: mostrar o cálculo(opcional)
    :return: O valor do fatorial ser um número n.
    """
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end="")
            if i > 1:
                print(' x ', end="")
            else:
                print(' = ', end="")
        f *= i
    return f


#Porgrama principal
print(fatorial(7, show=True))
help(fatorial)