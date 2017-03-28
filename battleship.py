import sys
from battle import battle
from blank_page import blank_page
from choose_winner import choose_winner
from count_x import count_x
from create_table import create_table
from draw_table import draw_table
from intro import intro
from place_ship import place_ship
from placement_options_check import placement_options_check
from reset_ship_dict import reset_ship_dict
from rules import rules
from shoot import shoot
from target import target

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

game_engine()