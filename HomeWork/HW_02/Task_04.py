"""
Напишите программу, которая принимает на вход 2 числа.
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях(не индексах).
Position one: 1
Position two: 3
Number of elements: 5
-> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
-> 15
"""

pos1 = int(input("Position one: "))
pos2 = int(input("Position two: "))
num = int(input("Number of elements: "))

ls = []

for i in range(-num, num):
    ls.append(i)

print(ls)
print(ls[pos1-1]*ls[pos2-1])