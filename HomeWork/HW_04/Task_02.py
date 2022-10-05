"""
Задайте натуральное число N.
Напишите программу, которая составит список простых множителей числа N.
Простые делители числа
in
54
out
[2, 3, 3, 3]
in
9990
out
[2, 3, 3, 3, 5, 37]
in
650
out
[2, 5, 5, 13]
"""


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def prime_factors(number):
    if is_prime(number):
        return 'Это простое число'

    factor = 2
    ls = []
    while number != 1:
        if is_prime(factor) and number % factor == 0:
            number /= factor
            ls.append(factor)
        else:
            factor += 1

    return ls


num = int(input())
print(prime_factors(num))