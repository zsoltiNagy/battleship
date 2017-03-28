import sys

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
table_1 = []
table_2 = []
if len(sys.argv) == 3:
    player_1 = sys.argv[1]
    player_2 = sys.argv[2]
else:
    player_1 = 'Player1'
    player_2 = 'Player2'