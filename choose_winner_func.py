from globals import *
from other_minor_func import *


def choose_winner(table_1, table_2):  # how can we make this smaller?
    print("\n" * 40)
    print('\n{}: {}'.format(player_1, count_x(table_1)))
    print('{}: {}'.format(player_2, count_x(table_2)))
    if count_x(table_1) > count_x(table_2):
        print('Player 1 ({}) won!'.format(player_1))
    elif count_x(table_1) < count_x(table_2):
        print('Player 2 ({}) won!'.format(player_2))
    else:
        print('Draw!')


def count_x(table):
    return sum([i.count('X') for i in table])
