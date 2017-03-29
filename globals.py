import sys

####################
# global variables #
####################

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
table_1 = []
table_2 = []

old_ship_dict = {  # rewrite!
    "Carrier": [5, 1],
    "Battleship": [4, 1],
    "Cruiser": [3, 2],
    "Destroyer": [2, 3]
}

ship_dict = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser_1": 3,
    "Cruiser_2": 3,
    "Destroyer_1": 2,
    "Destroyer_2": 2,
    "Destroyer_3": 2,
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
