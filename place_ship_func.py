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
