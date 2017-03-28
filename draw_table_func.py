def draw_table(table, *player):
    print_ship_pos = True
    try:
        if player[0] == player_1 and table == table_2 or player[0] == player_2 and table == table_1:
            print_ship_pos = False
    except IndexError:
        pass

    str_abc = ''
    str_abc = ' '.join(abc)

    print('      ', str_abc, '\n', ' '*50)

    str_table = ''
    str_table_list = []

    for i in table:
        str_table = ''.join(i)
        str_table = list(str_table)
        for j in str_table:
            if not print_ship_pos and j == 'X':
                str_table[str_table.index(j)] = '~'
        str_table = ' '.join(str_table)
        str_table_list.append(str_table)

    for i in range(1, 10):
        print('  ', i, ' ', str_table_list[i-1])
    print(' ', 10, ' ', str_table_list[9], '\n\n')
