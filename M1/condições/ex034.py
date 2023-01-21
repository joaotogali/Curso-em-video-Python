import math
sal = int(input('Qual o salario do funcionario:R$'))
if sal <= 1250:
    sal_novo = sal * 1.15
    print('o funcionario passa a ganhar:R${}'.format(sal_novo))
if sal > 1250:
    sal_novo = sal * 1.1
    print('O funcionario passa a ganhar:R${}'.format(sal_novo))
