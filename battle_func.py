from globals import *
from other_minor_func import *


def battle(player, player_table, opponent_table):
    blank_page(player)
    print(' ', '#' * 30, '\nThis is the opponents table\n', '#' * 29)  # rjust!
    draw_table(opponent_table, player)
    print(' ', '#' * 19, '\nThis your table\n', '#' * 19)  # rjust!
    draw_table(player_table, player)
    shoot(opponent_table)
    draw_table(opponent_table, player)
    input()


def shoot(table):
    while True:
        print('Choose your shooting coordinates!\n')
        let = ''
        while let not in abc:
            let = input('Vertical position (A-J): ')

        num = ''
        while num not in range(1, 11):
            num = input('Horizontal position (1-10): ')
            try:
                num = int(num)
                break
            except ValueError:
                pass
        break

    let = int(abc.index(let))
    num -= 1

    print(let, num)
    if table[num][let] == 'X':
        table[num][let] = 'H'
        pic = """
                         /\ 
                        /  \ 
                        \   \__
            _            \   \o\ 
           |_0            \   \o\=
~~~~~~~~~~~||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"""  # put every ascii_art into seperate file
    elif table[num][let] == '~':
        table[num][let] = 'O'
    # print(pic)
