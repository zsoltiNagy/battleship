from globals import *
from other_minor_func import *


def place_ship(table, ship_dict, player):
    blank_page(player)
    print('\nThis is the ship placement phase for {}!\n'.format(player).center(80, '#'))
    alt_ship_dict = ship_dict.copy()
    ships_left = 2  # 7 is original value, this should be maybe like a global value, so it would be easier to change
    # draw_table(table)
    while ships_left > 0:  # this is biggest while-loop I ever seen, mobydick
        print('These ships are still in your pool:')
        for ship in alt_ship_dict:
            print(ship, 'X' * alt_ship_dict[ship])
        print("\nYou can still place {} of 'em.".format(ships_left))
        for ship in alt_ship_dict:
            print('Now you have to place your {}'.format(ship))
            current_ship = ship
            ship_length = alt_ship_dict[ship]
            del alt_ship_dict[ship]
            break
        input()
        draw_table(table)

        let, num = place_first_part_of_ship(ship_length, table)  # we place the first dot here
        # ships_on_board[table] = [current_ship, ship_length, num, let]
        options = check_placement_options(let, num, ship_length, table)  # we check for options left and get a über-list
        dir_list = []  # we will fill this list with option names (like 'UP', 'DOWN', etc)
        direction = ''  # we will ask the user to input something to this string

        print('Which direction do you want to place your {}?\n'.format(current_ship))  # so we ask
        for i in options:  # we iterate through the options über-list we just got
            dir_list.append(i[0])  # we fill our empty list with valid input options
            print(i[0], '\n')  # then we print them out one-by-one on a new line to guide the user

        while direction not in dir_list:  # till we get the right input
            direction = input('> ')  # we prompt the user for one
        for i in options:  # we iterate through our über-list again
            if direction == i[0]:  # leaving this line out causes a strange bug, WTF
                if i[0] == 'UP':
                    draw_ship(table, i[3], i[2], i[1], True)
                if i[0] == 'DOWN':
                    draw_ship(table, i[2], i[3], i[1], True)
                if i[0] == 'LEFT':
                    draw_ship(table, i[3], i[2], i[1], False)
                if i[0] == 'RIGHT':
                    draw_ship(table, i[2], i[3], i[1], False)
                draw_table(table)
        ships_left -= 1
    input()
    return table


def check_placement_options(let, num, ship_length, table):
    x = ship_length - 1
    options = []

    # this is redundant as hell and a function nightmare
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
        options.append(['UP', let, end, start])

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
        options.append(['DOWN', let, start, end + 1])

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
        options.append(['LEFT', num, end, start])

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
        options.append(['RIGHT', num, start, end + 1])

    return options


def place_first_part_of_ship(ship_length, table):
    while True:
        print('Choose your starting coordinates!\n')
        let = ''
        while let not in abc:
            let = input('Vertical position (A-J): ')

        num = ''
        while num not in range(1, 11):
            num = input('Horizontal position (1-10): ')
            try:  # this and the while-loop its in just do the same, right?
                num = int(num)
            except ValueError:
                pass

        let = int(abc.index(let))
        num -= 1

        options = check_placement_options(let, num, ship_length, table)  # here we do a doblue check

        if table[num][let] != 'X' and len(options) >= 1:  # thats actually a pretty one
            table[num][let] = 'X'
            draw_table(table)
            return let, num
        else:
            print('\nThere is not enough space for this ship...\n')


def draw_ship(table, range_start, range_end, stable_coordinate, ver=True):
    for j in range(range_start, range_end):
        if ver:
            table[j][stable_coordinate] = 'X'
        else:
            table[stable_coordinate][j] = 'X'
    return table
