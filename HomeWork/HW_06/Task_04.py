"""Функция принимает в качестве аргументов строки в формате «Имя Фамилия»,
возвращает словарь, ключи — первые буквы фамилий, значения — словари,
реализованные по схеме предыдущего задания.
in
"Иван Сергеев", "Инна Серова", "Петр Алексеев",
"Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
"Борис Аркадьев", "Антон Серов", "Павел Анисимов"
out

{'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']},
'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']},
'И': {'И': ['Илья Иванов']}, 'В': {'Ю': ['Юнона Ветрякова']}}"""


def main(ls):
    dic = {}
    for name in ls:
        cur_ls = name.split()
        key_sur = cur_ls[1][0]
        key_nam = cur_ls[0][0]
        nam_dic = dic.setdefault(key_sur, {})
        name_ls = nam_dic.setdefault(key_nam, [])

        name_ls.append(name)
        nam_dic[key_nam] = name_ls
        dic[key_sur] = nam_dic

    print(dic)


text_ls = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
           "Борис Аркадьев", "Антон Серов", "Павел Анисимов"]
main(text_ls)
