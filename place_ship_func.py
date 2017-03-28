from globals import *
from other_minor_func import *

ship_dict = {
    "Carrier": [5, 1],
    "Battleship": [4, 1],
    "Cruiser": [3, 2],
    "Destroyer": [2, 3]
}


def place_ship(table, ship_dict, player):
    blank_page(player)
    print('#'*80, '\nThis is the ship placement phase for {}!\n'.format(player), '#'*79, '\n')
    reset_ship_dict()
    #  print(ship_dict)
    current_ship = ''
    ship_length = 0
    ships_left = 2  # 7
    draw_table(table)
    while ships_left > 0:
        print("Ships you can place: ", ships_left)
        for ship in ship_dict:
            if ship_dict[ship][1] > 0:
                print('\nYou still got {} {} ({}) left!\n'.format(ship_dict[ship][1],
                                                                  ship,
                                                                  'X'*ship_dict[ship][0]))
                current_ship = ship
                ship_length = ship_dict[ship][0]
                ship_dict[ship][1] -= 1
                break

        let, num = target(ship_length, table)
        options = placement_options_check(let, num, ship_length, table)
        dir_list = []
        direction = ''

        print('Which direction do you want to place your {}?\n'.format(current_ship))
        for i in options:
            dir_list.append(i[0])
            print(i[0], '\n')

        while direction not in dir_list:
            direction = input('> ')

        for i in options:
            if direction == i[0]:
                # UP
                if direction == 'UP' or direction == 'u':
                    for j in range(i[3], i[2]):
                        table[j][i[1]] = 'X'
                    draw_table(table)
                # DOWN
                if direction == 'DOWN' or direction == 'd':
                    for j in range(i[2], i[3]):
                        table[j][i[1]] = 'X'
                    draw_table(table)
                # LEFT
                if direction == 'LEFT' or direction == 'l':
                    for j in range(i[3], i[2]):
                        table[i[1]][j] = 'X'
                    draw_table(table)
                # RIGHT
                if direction == 'RIGHT' or direction == 'r':
                    for j in range(i[2], i[3]):
                        table[i[1]][j] = 'X'
                    draw_table(table)
        ships_left -= 1
    input()
    return table


def placement_options_check(let, num, ship_length, table):
    x = ship_length - 1
    options = []

    # UP
    up = False
    s = num
    e = num - x
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
        for i in range(s+1, e):
            if table[i][let] != '~':
                down = False
    except IndexError:
        pass
    if down:
        options.append(['DOWN', let, s, e+1])

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
        for i in range(s+1, e):
            if table[num][i] != '~':
                right = False
    except IndexError:
        pass
    if right:
        options.append(['RIGHT', num, s, e+1])

    return options


def reset_ship_dict():
    ship_dict["Destroyer"][1] = 3
    ship_dict["Carrier"][1] = 1
    ship_dict["Battleship"][1] = 1
    ship_dict["Cruiser"][1] = 2


def target(ship_length, table):
    global abc
    while True:
        print('Choose your starting coordinates!\n')
        let = ''
        while let not in abc:
            let = input('Vertical position (A-J): ')

        num = ''
        while num not in range(1, 11):
            num = input('Horizontal position (1-10): ')
            try:
                num = int(num)
            except ValueError:
                pass

        let = int(abc.index(let))
        num -= 1

        options = placement_options_check(let, num, ship_length, table)

        if table[num][let] != 'X' and len(options) >= 1:
            table[num][let] = 'X'
            draw_table(table)
            return let, num

        else:
            print('\nThere is not enough space for this ship...\n')        