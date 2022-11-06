
def turn_clockwise(x):                                              # 1
    if x == 'N':
        print('E')
    elif x == 'E':
        print('S')
    elif x == 'S':
        print('W')
    elif x == 'W':
        print('N')
    else:
        print('Input is not a compass point.')

user_input = input('Enter a compass point: ')

turn_clockwise(user_input)

print(turn_clockwise('N')=='E')

