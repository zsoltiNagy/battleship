def count_x(table):
    num = 0
    for i in table:
        for j in i:
            if j == 'X':
                num += 1
    return num