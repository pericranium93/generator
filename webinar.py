import sys

path_1, path_2 = sys.argv[1:]  # sys.argv[0] является именем скрипта
print(f'Копирую из папки {path_1} в папку {path_2}')

# import sys
#
# if 'h' in sys.argv[1:] or 'help' in sys.argv[1:]:
#     print('Описание как работать с вашим скриптом')
# else:
#     path_1, path_2 = sys.argv[1:]
#     print(f'Копирую из папки {path_1} в папку {path_2}')
#
# import argparse  # sys на максималках
#
# ################ГЕНЕРАТОРЫ########################
#
# old_list = [1, 2, 2, 2, 3, 4, 4, 4, 5]
# new_list = [x ** 2 + 1 for x in old_list if x % 2 == 0]  # генератор списка условие(if) можно не задавать
# print(new_list)
# new_set = {x ** 2 + 1 for x in old_list if x % 2 == 0}  # генератор множества
# new_dict = {x: x ** 2 + 1 for x in old_list if x % 2 == 0}  # генератор словаря
#
#
# def generator():  # Шаблон генератора Объекты НЕ ФОРМИРУЮТСЯ!
#     z = 0
#     while True:
#         z += 1
#         yield z
#
#
# g_obj = generator()  # здесь формируется генераторный объект вида <generator object ... >
#
# for i in g_obj:  # генератор с yield начинает работать и генерировать объекты только в тот момент, когда обращаются к объекту, который он генерирует
#     print(i)
#
# #####################################################
#
# import functools
#
# from functools import reduce, partial
#
#
# def my_f(num1, num2):
#     return num1 + num2
#
#
# print(reduce(my_f, [10, 20,
#                     30]))  # берет первые 2 значения, затем полученный результат и 3 значение и т.д. до окончания
#                            # последовательности
#
#
# def my_f(p1, p2):
#     return p1 - 1 ** p2 + 2
#
#
# new_func = partial(my_f, 2)  # Используется в том случае, если у нас есть пока что только один аргумент, а второй будет позже
# print(new_func)  # выводит объект вида <function my_f at 0x0.77...., 2>
# print(new_func(5))  # выводит конечный результат функции со вторым аргументом = 5
#

# from itertools import count, cycle
#
# for i in count(start=0, step=1):  # бесконечный цикл необходимо останавливать. отличие от range в том, что range конечен
#     print(i)
#     if i > 100:
#         break
#
# colors = ['red', 'yellow', 'green', 'yellow']  # бесконечно будет идти по последовательности.
# for i in cycle(colors):
#     print(i)
#
# import random
#
# random.seed(7)  # передаем в рандом ядро = 7, тогда все рандомы будут генерировать одно и то же число
# print(random.random())  # float от 0 до 1
# print(random.random(0, 5))  # int от 0 до 5 [0;5)
# print(random.random(0, 9, 3))  # int от 0 до 9 с шагом 3 [0;9)
