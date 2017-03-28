from intro_func import *
import sys
from battle_func import *
from choose_winner_func import *
from place_ship_func import *

####################
# global variables #
####################


################
# player names #
################



###############
# game engine #
###############
def game_engine():
    intro()
    place_ship(table_1, ship_dict, player_1)
    place_ship(table_2, ship_dict, player_2)
    turn = 0
    while turn < 3:
        battle(player_1, table_1, table_2)
        battle(player_2, table_2, table_1)
        turn += 1
    choose_winner(table_1, table_2)

if __name__ == "__main__":
    game_engine()
