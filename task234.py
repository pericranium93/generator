
'Задача 2'

a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
m = [j for i, j in zip(a, a[1:]) if j > i]
print(m)


'Задача 3'

print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])


'Задача 4'

a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
m = [i for i in a if a.count(i) == 1]
print(m)
