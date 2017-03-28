def shoot(table):
    while True:
        print('Choose your shooting coordinates!\n')
        let = ''
        while let not in abc:
            let = input('Vertical position (A-J): ')

        num = ''
        while num not in range(1, 11):
            num = input('Horizontal position (1-10): ')
            try:
                num = int(num)
                break
            except ValueError:
                pass
        break

    let = int(abc.index(let))
    num -= 1

    pic = ''
    print(let, num)
    if table[num][let] == 'X':
        table[num][let] = 'H'
        pic = """
                         /\ 
                        /  \ 
                        \   \__
            _            \   \o\ 
           |_0            \   \o\=
~~~~~~~~~~~||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"""
    elif table[num][let] == '~':
        table[num][let] = 'O'
    print(pic)