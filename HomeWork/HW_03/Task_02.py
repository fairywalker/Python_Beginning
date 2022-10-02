"""
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
in
4
out
[2, 5, 8, 10]
[20, 40]
"""
from random import randrange


def create_list(count):
    random_list = []
    for i in range(count):
        random_list.append(randrange(10))
    print(random_list)
    return random_list


def sum_of_opposite(count, list_numbers):
    middle = count // 2
    result = []

    for i in range(middle):
        result.append(list_numbers[i] + list_numbers[count - i - 1])

    if count % 2 != 0:
        result.append(list_numbers[middle])

    return result


n = int(input())
ls = create_list(n)
print(sum_of_opposite(n, ls))
