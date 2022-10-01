"""
Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
10
-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
-> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
"""
import random

n = int(input())
ls = []

for i in range(n):
    ls.append(i)

print(ls)

usedIndexes = []
result = []

while len(result) != n:
    currentIndex = random.randrange(0, n)
    if not (currentIndex in usedIndexes):
        result.append(ls[currentIndex])
        usedIndexes.append(currentIndex)

print(result)