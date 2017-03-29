from globals import *
from other_minor_func import *


def place_ship(table, ship_dict, player):
    blank_page(player)
    print('\nThis is the ship placement phase for {}!\n'.format(player).center(80, '#'))
    ship_dict_local = ship_dict.copy()
    ships_left = 2  # 7 is original value, this should be maybe like a global value, so it would be easier to change
    draw_table(table)
    while ships_left > 0:  # this is biggest while-loop I ever seen, mobydick
        print("Ships you can place: ", ships_left)
        for ship in ship_dict_local:  # THINK ABOUT THIS A LITTLE BIT
            if ship_dict_local[ship][1] > 0:
                print('\nYou still got {} {} ({}) left!\n'.format(ship_dict_local[ship][1],
                                                                  ship,
                                                                  'X' * ship_dict_local[ship][0]))
                current_ship = ship
                ship_length = ship_dict_local[ship][0]
                ship_dict_local[ship][1] -= 1
                break

        let, num = place_first_part_of_ship(ship_length, table)  # we place the first dot here
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
                # here we check what is the input and draw a lot of X to that direction as long as ship-length(x)
                # its redundant as hell of course
                # a clever for-loop would be nice
                # though maybe we have to redesign this whole process
                # UP
                if direction == 'UP':
                    for j in range(i[3], i[2]):
                        table[j][i[1]] = 'X'
                    draw_table(table)  # I think it's enough to put this line once on the end of this mess
                # DOWN
                if direction == 'DOWN':
                    for j in range(i[2], i[3]):
                        table[j][i[1]] = 'X'
                    draw_table(table)
                # LEFT
                if direction == 'LEFT':
                    for j in range(i[3], i[2]):
                        table[i[1]][j] = 'X'
                    draw_table(table)
                # RIGHT
                if direction == 'RIGHT':
                    for j in range(i[2], i[3]):
                        table[i[1]][j] = 'X'
                    draw_table(table)
        ships_left -= 1
    input()
    return table


def check_placement_options(let, num, ship_length, table):
    x = ship_length - 1  # why? maybe cause we already place an X in target() ...
    options = []

    # this is redundant as hell
    # UP
    up = False  # an empty variable is False too
    s = num  # up-down duplicate
    e = num - x  # also we will need better variable names
    if e >= 0:
        up = True
    for i in range(e, s):
        if table[i][let] != '~':
            up = False
    if up:
        options.append(['UP', let, s, e])

    # DOWN
    down = False
    s = num
    e = num + x
    if e <= 9:
        down = True
    try:
        for i in range(s + 1, e):
            if table[i][let] != '~':
                down = False
    except IndexError:
        pass
    if down:
        options.append(['DOWN', let, s, e + 1])

    # LEFT
    left = False
    s = let
    e = let - x
    if e >= 0:
        left = True
    for i in range(e, s):
        if table[num][i] != '~':
            left = False
    if left:
        options.append(['LEFT', num, s, e])

    # RIGHT
    right = False
    s = let
    e = let + x
    if e <= 9:
        right = True
    try:
        for i in range(s + 1, e):
            if table[num][i] != '~':
                right = False
    except IndexError:
        pass
    if right:
        options.append(['RIGHT', num, s, e + 1])

    return options


def place_first_part_of_ship(ship_length, table):  # we will need a more accurate name for this one
    while True:  # we need to do this to let the user make mistakes
        print('Choose your starting coordinates!\n')  # we need a more user-friendly solution for this
        let = ''  # let my hand rot if I name a variable like this again
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
