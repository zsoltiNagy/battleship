from globals import *
from other_minor_func import *
import random


def place_ship(table, ship_dict, player, AI=False):
    if not AI:
        blank_page(player)
        print('#This is the ship placement phase for {}!#'.format(player).center(144, '#'))
        print('\n')
    local_ship_dict = ship_dict.copy()
    ships_left = 7
    while ships_left > 0:
        if not AI:
            print('These ships are still in your pool: '.center(142, ' '))
            print('\n')
            for ship in local_ship_dict:
                print("{}{}{}".format(ship, '    ', 'X' * local_ship_dict[ship]).center(142, ' '))
        print('\n')
        print("You can still place {} of 'em.".format(ships_left).center(142, ' '))
        for ship in local_ship_dict:
            if not AI:
                print('\n')
                print('Now you have to place your {}'.format(ship).center(142, ' '))
                print('\n')
            current_ship = ship
            ship_length = local_ship_dict[ship]
            del local_ship_dict[ship]
            break
        if not AI:
            input('> '.rjust(70, ' '))
            draw_table(table)

        try:
            let, num = place_first_part_of_ship(ship_length, table, AI)
        except TypeError:
            pass
        options = check_placement_options(let, num, ship_length, table)
        dir_list = []
        direction = ''

#         if not AI:
#             print((direction_keys[i[0]] + '    ' + i[0]).center(142, ' '))

        for i in options:
            dir_list.append(i[0])
            if not AI:
                print((direction_keys[i[0]] + '    ' + i[0]).center(142, ' '))

        if not AI:
            while direction not in dir_list:
                direction = input('> '.rjust(70, ' '))
        else:
            direction = random.choice(dir_list)

        for i in options:
            if direction == i[0]:
                if i[0] == 'w':
                    draw_ship(table, i[3], i[2], i[1], True)
                if i[0] == 's':
                    draw_ship(table, i[2], i[3], i[1], True)
                if i[0] == 'a':
                    draw_ship(table, i[3], i[2], i[1], False)
                if i[0] == 'd':
                    draw_ship(table, i[2], i[3], i[1], False)
                if not AI:
                    draw_table(table)
        ships_left -= 1
    if not AI:
        input('> '.rjust(70, ' '))
        draw_table(table)
        input('> '.rjust(70, ' '))
    return table


def check_placement_options(let, num, ship_length, table):
    x = ship_length - 1
    options = []

    # this is redundant as hell and a to make a function out of it seems like a nightmare
    # UP
    up = False
    start = num - x
    end = num
    if start >= 0:
        up = True
    for i in range(start, end):
        if table[i][let] != '~':
            up = False
    if up:
        options.append(['w', let, end, start])

    # DOWN
    down = False
    start = num
    end = num + x
    if end <= 9:
        down = True
    try:
        for i in range(start + 1, end):
            if table[i][let] != '~':
                down = False
    except IndexError:
        pass
    if down:
        options.append(['s', let, start, end + 1])

    # LEFT
    left = False
    end = let
    start = let - x
    if start >= 0:
        left = True
    for i in range(start, end):
        if table[num][i] != '~':
            left = False
    if left:
        options.append(['a', num, end, start])

    # RIGHT
    right = False
    start = let
    end = let + x
    if end <= 9:
        right = True
    try:
        for i in range(start + 1, end):
            if table[num][i] != '~':
                right = False
    except IndexError:
        pass
    if right:
        options.append(['d', num, start, end + 1])

    return options


def place_first_part_of_ship(ship_length, table, AI=False):
    if not AI:
        let, num = valid_input()
        let = int(abc.index(let))
        num -= 1
    else:
        num = random.randint(0, 9)
        let = random.randint(0, 9)

    options = check_placement_options(let, num, ship_length, table)

    if table[num][let] != 'X' and len(options) >= 1:
        table[num][let] = 'X'
        if not AI:
            draw_table(table)
        return let, num
    else:
        if not AI:
            print('\n')
            print('There is not enough space for this ship...'.center(142, ' '))
            print('\n')


def draw_ship(table, range_start, range_end, stable_coordinate, ver=True):
    for j in range(range_start, range_end):
        if ver:
            table[j][stable_coordinate] = 'X'
        else:
            table[stable_coordinate][j] = 'X'
    return table
