"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
- 4 -> [1, 2, 6, 24]
- 6 -> [1, 2, 6, 24, 120, 720]

"""
n = int(input())
ls = []
temp = 1;

for i in range(1, n+1):
    temp = temp * i
    ls.append(temp)

print(ls)