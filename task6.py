import sys
from itertools import count, cycle

number, user_list = sys.argv[1:]
number = int(number)

user_list = list(user_list)
n = 0

for i in count(number, 1):
    print(i)
    if i == 100:
        break

for i in cycle(user_list):
    print(i)
    stop = input('Введите "q", чтобы закончить цикл')  # украл у вас из объяснения
    if stop == 'q':
        break


