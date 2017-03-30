from globals import *
from ASCII_art import blank_page_art
import os


def blank_page(player):
    os.system('clear')
    blank_page_art()
    c = ("\nThis is {}'s turn. \nPress any key to continue...\n".format(player))
    lines = str(c).split('\n')
    for i in lines:
        print(i.center(142, ' '))
    input('> '.rjust(70, ' '))
    print("\n" * 40)


def draw_table(table, *player):
    print_ship_pos = True
    try:
        if player[0] == player_1 and table == table_2 or player[0] == player_2 and table == table_1:
            print_ship_pos = False
    except IndexError:
        pass

    str_abc = ''
    str_abc = ' '.join(abc)

    print("{}\n".format(str_abc).center(144, ' '))

    str_table_list = []

    for i in table:
        str_table = ''.join(i)
        str_table = list(str_table)
        for j in str_table:
            if not print_ship_pos and j == 'X':
                str_table[str_table.index(j)] = '~'
        str_table = ' '.join(str_table)
        str_table_list.append(str_table)

    width = 70
    for i in range(1, 10):
        print("{}{}{}".format(i, ' ', str_table_list[i - 1]).center(142, ' '))
    print("{}{}{}".format(10, ' ', str_table_list[i - 1]).center(140, ' '))
    print('\n')


def valid_input():
    coordinates_valid = False
    while coordinates_valid is False:
        coor = input("Choose your coordinates here: ".rjust(85, ' '))
        try:
            if len(coor) == 2:
                num = int(coor[1])
            else:
                num = int(str(coor[1] + coor[2]))
            let = coor[0]
            let = let.upper()
        except SyntaxError:
            continue
        except ValueError:
            continue
        except IndexError:
            continue
        except TypeError:
            continue

        if let in abc and num in range(1, 11):
            coordinates_valid = True
            return let, num
