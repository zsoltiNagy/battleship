def choose_winner(table_1, table_2):
    if count_x(table_1) > count_x(table_2):
        print('Player 1 won!')
    elif count_x(table_1) < count_x(table_2):
        print('Player 2 won!')
    else:
        print('Draw!')

