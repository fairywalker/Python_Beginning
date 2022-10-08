"""
Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
in
Number of words: 10
out
авб абв бав абв вба бав вба абв абв абв
авб бав вба бав вба
"""

from random import choices


def fill_list(num):
    result = []
    for i in range(num):
        result.append("".join(choices("абв", k=3)))
    return " ".join(result)


def remove_abc(lis):
    return lis.replace("абв", "").replace("  ", " ")


n = int(input("Number of words: "))
ls = fill_list(n)
print(ls)
print(remove_abc(ls))



