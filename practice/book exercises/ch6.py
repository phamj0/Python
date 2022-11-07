
def turn_clockwise(x):                                                      # 1
    if x == 'N':
        print('E')
        return 'E'
    elif x == 'E':
        print('S')
        return 'S'
    elif x == 'S':
        print('W')
        return 'W'
    elif x == 'W':
        print('N')
        return 'N'
    else:
        print('Input is not a compass point.')

user_input = input('Enter a compass point: ')

turn_clockwise(user_input)

turn_clockwise('N')=='E'