"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
in
88
out
1011000
"""


def decimal_to_binary(number):
    list_of_digits = []
    while number > 0:
        list_of_digits.append(number % 2)
        number = number // 2

    result = 0;
    for i in range(len(list_of_digits)):
        result += list_of_digits[i] * (10 ** i)

    return result


n = int(input())
print(decimal_to_binary(n))
