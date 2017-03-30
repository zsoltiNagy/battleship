from globals import *
from other_minor_func import *
from ASCII_art import ship_hit_art


def battle(player, player_table, opponent_table):
    blank_page(player)
    print("\nThis is the opponent's table\n".center(90, '#'))
    draw_table(opponent_table, player)
    print("\nThis is your table\n".center(80, '#'))
    draw_table(player_table, player)
    shoot(opponent_table)
    draw_table(opponent_table, player)
    input()


def shoot(table):
    let, num = valid_input()

    let = int(abc.index(let))
    num -= 1

    print(let, num)
    if table[num][let] == 'X':
        table[num][let] = 'H'
        if not check_neighbouring_coordinates(table, let, num):
            print('You succesfully sunk an enemy ship!')
            print(ship_hit_art)
    elif table[num][let] == '~':
        table[num][let] = 'O'


def check_neighbouring_coordinates(table, let, num):
    if let > 0:
        if table[num][let - 1] == 'X':
            return True
    if let < 9:
        if table[num][let + 1] == 'X':
            return True
    if num > 0:
        if table[num - 1][let] == 'X':
            return True
    if let > 0:
        if table[num + 1][let] == 'X':
            return True
    return False
