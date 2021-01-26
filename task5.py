from functools import reduce


def my_f(n1, n2):
    return n1 * n2


a = [i for i in range(100, 1001) if i % 2 == 0]
print(a)
print(reduce(my_f, a))

a = [i for i in range(100, 1001) if i % 2 == 0]
print(a)
print(reduce(lambda n1, n2: n1 * n2, a))