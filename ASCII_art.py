def ship_hit_art():
    ship_hit = """
                             /\ 
                            /  \ 
                            \   \__
                _            \   \o\ 
               |_0            \   \o\=
    ~~~~~~~~~~~||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
    """
    lines = str(ship_hit).split('\n')
    for i in lines:
        print(i.center(142, ' '))


def intro_art():
    intro = """
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

    """
    lines = str(intro).split('\n')
    for i in lines:
        print(i.center(120, ' '))


def blank_page_art():
    blank_page_art = """
                                          # #  ( )
                                       ___#_#___|__
                                   _  |____________|  _
                            _=====| | |            | | |==== _
                      =====| |.---------------------------. | |====
        <--------------------'   .  .  .  .  .  .  .  .   '--------------/
          \                                                             /
           \___________________________________________________________/
       wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
     wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
        wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww 
    """
    lines = str(blank_page_art).split('\n')
    for i in lines:
        print(i.center(142, ' '))
