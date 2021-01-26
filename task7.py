from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)


n = int(input('Введите конечное число, для которого рассчитывается факториал'))

for i, el in enumerate(fact(n), 1):
    print(f'{i}! = {el}')
