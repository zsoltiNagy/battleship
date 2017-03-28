from globals import *

def intro():
    create_table(table_1)
    create_table(table_2)
    # For the sake of readability we should make a variable from this
    print("""
                     _           _   _   _           _     _
                    | |         | | | | | |         | |   (_)
                    | |__   __ _| |_| |_| | ___  ___| |__  _ _ __
                    | '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
                    | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
                    |_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/
                                                            | |
                                                            |_|

                                     |__
                                     |\/
                                     ---
                                     / | [
                              !      | |||
                            _/|     _/|-++'
                        +  +--|    |--|--|_ |-
                     { /|__|  |/\__|  |--- |||__/
                    +---------------___[}-_===_.'____                 /\ 
                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _
 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7
|                                                                     BB-61/
 \_________________________________________________________________________|

""".center(80, ' '))
    print("Welcome {} and {}!".format(player_1, player_2).center(80, ' '))
    rules()
    input()


def create_table(table):
    """
    Obviously its a function that creates tables.
    """
    for i in abc:
        i = []
        i = ['~'] * 10
        table.append(i)


def rules():
    print("""
    Defend the holy empire from the godless savages' vicious attacks.
    Sink as many of their ships as you can.First place your own ships, 
            wait for your turn, then launch your missiles!\n
    """.center(80, ' '))
    print("~: Sea       X: Ship     H: Ship hit     O: Miss".center(80, ' '))    