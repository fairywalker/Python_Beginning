"""
Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
in
5
out
[10, 2, 3, 8, 9]
22
"""

from random import randrange

def create_list(count):
    random_list = []
    for i in range(count):
        random_list.append(randrange(10))
    print(random_list)
    return random_list


def sum_of_odd(count, list_numbers):
    pos = 1
    result = 0
    while pos <= count:
        result += list_numbers[pos-1]
        pos += 2
    return result

n = int(input())
ls = create_list(n)
print(sum_of_odd(n, ls))
