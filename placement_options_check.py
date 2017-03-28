def placement_options_check(let, num, ship_length, table):
    x = ship_length - 1
    options = []

    # UP
    up = False
    s = num
    e = num - x
    if e >= 0:
        up = True
    for i in range(e, s):
        if table[i][let] != '~':
            up = False
    if up:
        options.append(['UP', let, s, e])

    # DOWN
    down = False
    s = num
    e = num + x
    if e <= 9:
        down = True
    try:
        for i in range(s+1, e):
            if table[i][let] != '~':
                down = False
    except IndexError:
        pass
    if down:
        options.append(['DOWN', let, s, e+1])

    # LEFT
    left = False
    s = let
    e = let - x
    if e >= 0:
        left = True
    for i in range(e, s):
        if table[num][i] != '~':
            left = False
    if left:
        options.append(['LEFT', num, s, e])

    # RIGHT
    right = False
    s = let
    e = let + x
    if e <= 9:
        right = True
    try:
        for i in range(s+1, e):
            if table[num][i] != '~':
                right = False
    except IndexError:
        pass
    if right:
        options.append(['RIGHT', num, s, e+1])

    return options