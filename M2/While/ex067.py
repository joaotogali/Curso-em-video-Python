
while True:
        num = int(input('QUer ver a tabuada de qual valor:'))
        if num < 0:
              break
        print('~'*30)
        for c in range(1,11):
                print(f'{num} x {c} = {num * c}')
        print('~' * 30)
print('Programa de tabuada encerrada')
