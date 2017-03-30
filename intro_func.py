from globals import *
from ASCII_art import intro_art


def intro():
    create_table(table_1)
    create_table(table_2)
    intro_art()
    print("Welcome {} and {}!".format(player_1, player_2).center(142, ' '))
    rules()
    input('> '.rjust(70, ' '))


def create_table(table):
    for i in abc:
        i = ['~'] * 10
        table.append(i)


def rules():
    text_rules = """
        Defend the holy empire from the godless savages' vicious attacks.
        Sink as many of their ships as you can.First place your own ships,
        wait for your turn, then launch your missiles!\n
        """
    lines = str(text_rules).split('\n')
    for i in lines:
        print(i.center(142, ' '))

    print("~: Sea       X: Ship     H: Ship hit     O: Miss".center(142, ' '))
