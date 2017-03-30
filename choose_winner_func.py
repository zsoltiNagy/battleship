from globals import *
from other_minor_func import *


def choose_winner(table_1, table_2):  # how can we make this smaller?
    print("\n" * 40)
    print('\n{}: {}'.format(player_1, count_x(table_1)))
    print('{}: {}'.format(player_2, count_x(table_2)))
    if count_x(table_1) > count_x(table_2):
        print('Player 1 ({}) won!'.format(player_1))
        export_score(player_1, count_x(table_1))
    elif count_x(table_1) < count_x(table_2):
        print('Player 2 ({}) won!'.format(player_2))
        export_score(player_2, count_x(table_2))
    else:
        print('Draw!')
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
    #print(highscore, type(highscore))
    print('HIGHSCORES')
    for i in highscore:
        print(i[0], i[1])