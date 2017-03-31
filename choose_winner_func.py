from globals import *
from other_minor_func import *


def choose_winner(table_1, table_2):
    print("\n" * 40)
    input('> '.rjust(70, ' '))
    print('{}: {}'.format(player_1, count_x(table_1)).center(142, ' '))
    print('\n')
    print('{}: {}'.format(player_2, count_x(table_2)).center(142, ' '))
    print('\n')
    if count_x(table_1) > count_x(table_2):
        print('({}) won!'.format(player_1).center(142, ' '))
        export_score(player_1, count_x(table_1))
    elif count_x(table_1) < count_x(table_2):
        print('({}) won!'.format(player_2).center(142, ' '))
        export_score(player_2, count_x(table_2))
    else:
        print('Draw!'.center(142, ' '))
        export_score(player_1, count_x(table_1))
        export_score(player_2, count_x(table_2))
    import_highscores()


def count_x(table):
    return sum([i.count('X') for i in table])


def export_score(winner, points, filename="highscore.txt"):
    new_line = winner + '~' + str(points) + '\n'
    with open(filename, 'a') as f:
        f.write(new_line)


def import_highscores(filename="highscore.txt"):
    highscore = []
    with open(filename, 'r') as f:
        content = f.readlines()
    for line in content:
        line = line.strip('\n').split('~')
        highscore.append(line)

    print('HIGHSCORES'.center(142, ' '))
    for i in highscore:
        print(i[0].center(142, ' '), i[1].center(162, ' '))
