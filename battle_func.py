def battle(player, player_table, opponent_table):
    blank_page(player)
    print(' ', '#'*30, '\nThis is the opponents table\n', '#'*29)
    draw_table(opponent_table, player)
    print(' ', '#'*19, '\nThis your table\n', '#'*19)
    draw_table(player_table, player)
    shoot(opponent_table)
    draw_table(opponent_table, player)
    input()
