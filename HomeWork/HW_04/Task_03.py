"""
Задайте последовательность чисел. Напишите программу,
которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
in
7
out
[4, 5, 3, 3, 4, 1, 2]
[5, 1, 2]
in
-1
out
Negative value of the number of numbers!
[]
in
10
out
[4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
[6, 2, 3, 0, 9]
"""

from random import randrange
from collections import Counter


def get_random_list(number):
    ls = []
    if number < 0:
        return ls

    for i in range(number):
        ls.append(randrange(0, number // 2))
    print(ls)
    return ls


def get_unique_values(values):
    cnt = Counter(values)
    ls = []
    for val in values:
        if cnt.get(val) == 1:
            ls.append(val)
    return ls

def task_03(number):
    if number < 0:
        return("Negative value of the number of numbers!")
    return get_unique_values(get_random_list(number))


n = int(input())

print(task_03(n))
