import sys

####################
# global variables #
####################

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
table_1 = []
table_2 = []

ship_dict = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser I": 3,
    "Cruiser II": 3,
    "Destroyer I": 2,
    "Destroyer II": 2,
    "Destroyer III": 2
}

direction_keys = {
    "w": 'UP',
    "a": 'LEFT',
    "s": 'DOWN',
    "d": 'RIGHT'
}


#########################
# player names and "AI" #
#########################

AI_1 = False
AI_2 = False
AI_1_next_target = []
AI_2_next_target = []

if len(sys.argv) == 3:
    player_1 = sys.argv[1]
    if sys.argv[1] == 'AI1':
        AI_1 = True
    player_2 = sys.argv[2]
    if sys.argv[2] == 'AI2':
        AI_2 = True
else:
    player_1 = 'Player1'
    player_2 = 'Player2'

