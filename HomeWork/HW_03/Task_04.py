"""
Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
in
5
out
[5.16, 8.62, 6.57, 7.92, 9.22]
Min: 0.16, Max: 0.92. Difference: 0.76
"""

from random import uniform


def create_float_list(count):
    random_list = []
    for i in range(count):
        random_list.append(round(uniform(0, 10), 2))
    print(random_list)
    return random_list


def min_max_diff(count, list_of_nums):

    min_part = float(1)
    max_part = float(0)

    for i in (range(count)):
        remainder = round(list_of_nums[i] % 1, 2)
        if remainder > max_part:
            max_part = remainder
        if remainder < min_part:
            min_part = remainder
    return round(max_part - min_part,2)


n = int(input())
ls = create_float_list(n)
print(min_max_diff(n, ls))
