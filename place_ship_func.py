from globals import *
from other_minor_func import *
import random


def place_ship(table, ship_dict, player, AI=False):
    blank_page(player)
    print('\n#This is the ship placement phase for {}!#\n'.format(player).center(142, '#'))
    local_ship_dict = ship_dict.copy()
    ships_left = 7  # 7 is original value, this should be maybe like a global value, so it would be easier to change
    # draw_table(table)
    while ships_left > 0:  # this is biggest while-loop I ever seen, mobydick
        if not AI:
            print('\nThese ships are still in your pool:\n')
            for ship in local_ship_dict:
                print(ship.rjust(15), ('X' * local_ship_dict[ship]).rjust(10))
            print("\n\t\tYou can still place {} of 'em.".format(ships_left))
        for ship in local_ship_dict:
            if not AI:
                print('\t\tNow you have to place your {}'.format(ship))
            current_ship = ship
            ship_length = local_ship_dict[ship]
            del local_ship_dict[ship]
            break
        if not AI:
            input()
        draw_table(table)

        let, num = place_first_part_of_ship(ship_length, table, AI)  # we place the first dot here
        options = check_placement_options(let, num, ship_length, table)  # we check for options left and get a über-list
        dir_list = []  # we will fill this list with option names (like 'UP', 'DOWN', etc)
        direction = ''  # we will ask the user to input something to this string

        print('Which direction do you want to place your {}?\n'.format(current_ship))  # so we ask
        for i in options:  # we iterate through the options über-list we just got
            dir_list.append(i[0])  # we fill our empty list with valid input options
            print(direction_keys[i[0]], '  ('.rjust(10-len(direction_keys[i[0]])), i[0], ')', '\n')
        if not AI:
            while direction not in dir_list:  # till we get the right input
                direction = input('> ')  # we prompt the user for one
        else:
            direction = random.choice(dir_list)
        for i in options:  # we iterate through our über-list again
            if direction == i[0]:  # leaving this line out causes a strange bug, WTF
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
        input()
    draw_table(table)
    input()
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
        draw_table(table)
        return let, num
    else:
        if not AI:
            print('\nThere is not enough space for this ship...\n')


def draw_ship(table, range_start, range_end, stable_coordinate, ver=True):
    for j in range(range_start, range_end):
        if ver:
            table[j][stable_coordinate] = 'X'
        else:
            table[stable_coordinate][j] = 'X'
    return table
