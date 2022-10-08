"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
Алгоритм RLE
in
Enter the name of the file with the text:
'text_words.txt'
Enter the file name to record:
'text_code_words.txt'
Enter the name of the file to decode:
'text_code_words.txt'
out
aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
"""
from os.path import exists


def main():
    files = inputs()
    if not check_file(files["file_text"]):
        return
    code_file(files)
    decode_file(files)
    print("Done!")


def decode_file(files):
    with open(files["file_record"], "r", encoding="utf-8") as file_record:
        with open(files["file_decode"], "w", encoding="utf-8") as file_decode:
            for line in file_record:
                file_decode.write(decode_text(line) + "\n")


def decode_text(text):
    text = text.replace("\n", "")
    res = ""
    count_str = ""
    for i in text:
        if i.isdigit():
            count_str = count_str + i
        else:
            count = int(count_str)
            for j in range(count):
                res = res + i
            count_str = ""
    return res


def code_file(files):
    with open(files["file_text"], "r", encoding="utf-8") as file_text:
        with open(files["file_record"], "w", encoding="utf-8") as file_record:
            for line in file_text:
                file_record.write(code_text(line))


def code_text(text):
    res = ""
    cur = text[0]
    count = 0;
    for i in text:
        if i != cur:
            res = res + str(count) + cur
            cur = i
            count = 1
        else:
            count += 1

    res = res + str(count) + cur

    return res


def check_file(name):
    if not exists(name):
        print(f'File {name} does not exist!')
        return False
    return True


def inputs():
    file_text = input("Enter the name of the file with the text:\n")
    file_record = input("Enter the file name to record:\n")
    file_decode = input("Enter the name of the file to decode:\n")

    # print("Enter the name of the file with the text:")
    # file_text = 'text_words.txt'
    # print(file_text)
    # print("Enter the file name to record:")
    # file_record = 'text_code_words.txt'
    # print(file_record)
    # print("Enter the name of the file to decode:")
    # file_decode = 'text_decode_words.txt'
    # print(file_decode)

    dict_files = {
        "file_text": file_text,
        "file_record": file_record,
        "file_decode": file_decode
    }

    return dict_files


main()
