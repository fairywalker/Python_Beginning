"""
Даны два файла, в каждом из которых находится запись многочленов.
Задача - сформировать файл, содержащий сумму многочленов.
in
"poly.txt"
"poly_2.txt"
out in the file
3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
in
"poly.txt"
"poly_2.txt"
out
The contents of the files do not match!
"""


def task_04():
    ls_1 = read_file('poly.txt')
    ls_2 = read_file('poly_2.txt')
    if len(ls_1) != len(ls_2):
        print('The contents of the files do not match!')
        return
    with open("task_05.txt", "w", encoding="utf-8") as output:
        for i in range(3):
            output.write(ls_1[i].replace('= 0', '+ ').replace('\n', '') + ls_2[i])


def read_file(name):
    with open(name, "r", encoding="utf-8") as output:
        ls = []
        for line in output:
            ls.append(line)
        output.close()
        return ls


task_04()
