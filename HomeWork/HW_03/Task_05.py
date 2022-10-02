"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Негафибоначчи

in
8
out
-21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
in
5
out
5 -3 2 -1 1 0 1 1 2 3 5
"""


def fill_fib(n):
    fib = [1, 0, 1]
    for i in range(3, n + 2):
        fib.append(fib[i - 1] + fib[i - 2])

    for i in range(n - 1):
        fib.insert(0, fib[1] - fib[0])

    return fib


n = int(input())
print(fill_fib(n))
