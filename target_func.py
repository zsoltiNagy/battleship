def target(ship_length, table):
    while True:
        print('Choose your starting coordinates!\n')
        let = ''
        while let not in abc:
            let = input('Vertical position (A-J): ')

        num = ''
        while num not in range(1, 11):
            num = input('Horizontal position (1-10): ')
            try:
                num = int(num)
            except ValueError:
                pass

        let = int(abc.index(let))
        num -= 1

        options = placement_options_check(let, num, ship_length, table)

        if table[num][let] != 'X' and len(options) >= 1:
            table[num][let] = 'X'
            draw_table(table)
            return let, num

        else:
            print('\nThere is not enough space for this ship...\n')