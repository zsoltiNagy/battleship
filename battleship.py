from intro_func import *
from battle_func import *
from choose_winner_func import *
from place_ship_func import *
import os

###############
# game engine #
###############


def game_engine():
    intro()
    os.system('clear')
    place_ship(table_1, ship_dict, player_1, AI_1)
    os.system('clear')
    place_ship(table_2, ship_dict, player_2, AI_2)
    os.system('clear')
    turn = 0
    while turn < 10:
        battle(player_1, table_1, table_2, AI_1)
        os.system('clear')
        battle(player_2, table_2, table_1, AI_2)
        os.system('clear')
        turn += 1
    choose_winner(table_1, table_2)


if __name__ == "__main__":  # michael scott will be always remembered!
    game_engine()
