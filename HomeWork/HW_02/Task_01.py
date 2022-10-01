"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
in -> out
- 6782 -> 23
- 0.67 -> 13
- 198.45 -> 27
"""

num = float(input())

# print(num % 1)

while num % 1 != 0:
    num *= 10

result = 0

while num != 0:
    result += int((num % 10))
    num = num // 10

print(result)