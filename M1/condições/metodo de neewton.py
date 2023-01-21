#algoritmo para descobrir o metodo de newton

a = 30
x = [None]*(a+1)

x[0] = - 0.5

def fd(x):
    y = (11*(x)**11) - 2*(x)**2 + 17
    return y

def derivada(x):
    y = (121*(x)**10) - 4*(x)
    return y


#calculo do método de newton

for j in range(a):
    x[j+1] = x[j] - fd(x[j])/derivada(x[j])
    print(x[j+1])
