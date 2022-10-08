
def main():

    values = list(range(1, 10))

    x_symbol = chr(10060)
    o_symbol = chr(11093)
    turn_number = 0

    turn = o_symbol

    while True:

        turn_number += 1

        if turn == o_symbol:
            turn = x_symbol
        else:
            turn = o_symbol

        draw_table(values)

        while True:
            print("Enter a number from 1 to 9.")
            value = input(f"Select a position {turn}")
            if check_val(value, values):
                break

        values[int(value)-1] = turn

        if game_over(values, turn, turn_number):
            return


def game_over(vals, tr, tr_n):

    ls = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    res = False

    mes = ""

    for i in ls:
        if vals[i[0]] == vals[i[1]] == vals[i[2]]:
            mes = f"{tr} - WIN {chr(127942)} {chr(127881)}"
            res = True

    if tr_n == 9:
        mes = f"Drawn game {chr(129318)} {chr(129309)}"
        res = True

    if res:
        draw_table(vals)
        print(mes)

    return res


def check_val(val, vals):

    error_message = f"Incorrect input {chr(9940)}. Are you sure you entered a correct number?"

    try:
        val_int = int(val)
    except ValueError:
        print(error_message)
        return False

    if not 0 < val_int < 10:
        print(error_message)
        return False

    if not vals[val_int-1] in range(10):
        print(f"This cell is already occupied {chr(9995)}{chr(129292)}")
        return False

    return True


def draw_table(values):
    print("\n" * 100)

    ls = []
    for i in values:
        if i in range(1, 10):
            ls.append(f" {i} ")
        else:
            ls.append(f"{i} ")

    print('\t-----------------')
    print("\t {}   {}   {}".format(ls[0], ls[1], ls[2]))
    print('\t-----------------')
    print("\t {}   {}   {}".format(ls[3], ls[4], ls[5]))
    print('\t-----------------')
    print("\t {}   {}   {}".format(ls[6], ls[7], ls[8]))
    print('\t-----------------')


main()
