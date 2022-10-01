"""
Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
"""

n = int(input())

ls = []

for i in range(1, n+1):

    ls.append(round((1 + 1/i) ** i))

print(ls)
print(sum(ls))