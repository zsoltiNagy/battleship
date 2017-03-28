from create_table_func import *
from intro_func import *
import sys
from battle_func import *
from blank_page_func import *
from choose_winner_func import *
from count_x_func import *
from draw_table_func import *
from place_ship_func import *
from placement_options_check_func import *
from reset_ship_dict_func import *
from rules_func import *
from shoot_func import *
from target_func import *

####################
# global variables #
####################

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
table_1 = []
table_2 = []

ship_dict = {
    "Carrier": [5, 1],
    "Battleship": [4, 1],
    "Cruiser": [3, 2],
    "Destroyer": [2, 3]
}

################
# player names #
################
if len(sys.argv) == 3:
    player_1 = sys.argv[1]
    player_2 = sys.argv[2]
else:
    player_1 = 'Player1'
    player_2 = 'Player2'


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
