from globals import *
from other_minor_func import *
from ASCII_art import ship_hit_art
import random


def battle(player, player_table, opponent_table, AI=False):
    if not AI:
        blank_page(player)
        print("######  This is the opponent's table  ######".center(142, ' '))
        draw_table(opponent_table, player)
        print("######  This is your table  ######".center(142, ' '))
        draw_table(player_table, player)
    shoot(opponent_table, player, AI)
    print("######  This is the opponent's table  ######".center(142, ' '))
    print('######  {} shot on this table.  ######'.format(player).center(142, ' '))
    draw_table(opponent_table, player)
    input('> '.rjust(70, ' '))
    blank_page(player)


def shoot(table, player, AI=False):
    global AI_1_next_target, AI_2_next_target
    if not AI:
        let, num = valid_input()
        let = int(abc.index(let))
        num -= 1
    elif player == 'AI1' and AI_1_next_target:
        num = AI_1_next_target[0][0]
        let = AI_1_next_target[0][1]
        del AI_1_next_target[0]
    elif player == 'AI2' and AI_2_next_target:
        num = AI_2_next_target[0][0]
        let = AI_2_next_target[0][1]
        del AI_2_next_target[0]
    else:
        num = random.randint(0, 9)
        let = random.randint(0, 9)

    if table[num][let] == 'X':
        table[num][let] = 'H'
        if not check_neighbouring_coordinates(table, let, num):
            print('You succesfully sunk an enemy ship!'.center(142, ' '))
            print(ship_hit_art())
        if AI and check_neighbouring_coordinates(table, let, num):
            if player == 'AI1':
                AI_1_next_target = possible_targets(num, let, table)
            elif player == 'AI2':
                AI_2_next_target = possible_targets(num, let, table)
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
    if num < 9:
        if table[num + 1][let] == 'X':
            return True
    return False


def possible_targets(num, let, table):
    possible_targets = []
    if let > 0 and table[num][let - 1] != 'H':
        possible_targets.append([num, let - 1])
    if let < 9 and table[num][let + 1] != 'H':
        possible_targets.append([num, let + 1])
    if num > 0 and table[num - 1][let] != 'H':
        possible_targets.append([num - 1, let])
    if num < 9 and table[num - 1][let] != 'H':
        possible_targets.append([num + 1, let])
    return possible_targets
