"""
Задана натуральная степень k.
Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
записать в файл полученный многочлен не менее 3-х раз.
in
9
5
3
out in the file
3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
4*x^2 - 4 = 0
in
0
-1
4
out in the file
3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
4*x^2 - 4 = 0
2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0
"""

from random import randrange
from random import choices


def get_random_list(number):
    ls = []
    for i in range(number):
        ls.append(randrange(0, 11))
    print(ls)
    return ls


def add_plus_minus(str_data):
    if str_data == '':
        return str_data
    return str_data + f" {choices('+-', k=1)[0]} "


def add_to_file(str_data):
    with open("task_04.txt", "a", encoding="utf-8") as output:
        output.write(str_data + '\n')


def task_04(number):
    if number < 1:
        return
    rand_ls = get_random_list(number)
    eq = ''
    while number >= -1:
        if rand_ls[number - 1] == 0:
            number -= 1
            continue
        elif number > 1:
            eq = add_plus_minus(eq)
            eq = eq + f'{rand_ls[number - 1]}*x^{number}'
        elif number == 1:
            eq = add_plus_minus(eq)
            eq = eq + f'{rand_ls[number - 1]}'
        elif number == 0:
            eq = eq + ' = 0'
        number -= 1

    print(eq)
    add_to_file(eq)


n = int(input())

task_04(n)
