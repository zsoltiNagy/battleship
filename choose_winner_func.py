from globals import *


def choose_winner(table_1, table_2):  # how can we make this smaller?
    if count_x(table_1) > count_x(table_2):
        print('Player 1 won!')
    elif count_x(table_1) < count_x(table_2):
        print('Player 2 won!')
    else:
        print('Draw!')


def count_x(table):
    return sum([i.count('X') for i in table])
