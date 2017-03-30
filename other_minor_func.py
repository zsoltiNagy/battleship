from globals import *
from ASCII_art import blank_page_art


def blank_page(player):  # we should replace this THING with the clear func
    print("\n" * 40)
    blank_page_art()
    c = input("\nThis is {}'s turn. \nPress any key to continue...\n> ".format(player).center(40, 'w'))
    print(c)
    print("\n" * 40)


def draw_table(table, *player):
    print_ship_pos = True
    try:
        if player[0] == player_1 and table == table_2 or player[0] == player_2 and table == table_1:  # can we make this smaller?
            print_ship_pos = False
    except IndexError:
        pass

    str_abc = ''
    str_abc = ' '.join(abc)

    print('      ', str_abc, '\n', ' ' * 50)

    str_table_list = []

    for i in table:  # we should name this more accuretally
        str_table = ''.join(i)
        str_table = list(str_table)
        for j in str_table:
            if not print_ship_pos and j == 'X':  # thats how wo make X disappear
                str_table[str_table.index(j)] = '~'
        str_table = ' '.join(str_table)  # to make our output nice
        str_table_list.append(str_table)

    width = 80
    for i in range(1, 11):
        print("{:>3}{:>3}{:>3}".format(i, ' ', str_table_list[i - 1], width))


def valid_input():
    coordinates_valid = False
    while coordinates_valid is False:
        coor = input("Choose your coordinates here: ")
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
        if let in abc and num in range(1, 11):
            coordinates_valid = True
            return let, num
