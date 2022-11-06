# Homework 3 Chapter 5

# 5. Complete this truth table:
# The following code prints out a 'truth table'
print('p  q  r\t\t(not (p and q)) or r')

print('F  F  F\t\t T')
print('F  F  T\t\t T')
print('F  T  F\t\t T')
print('F  T  T\t\t T')
print('T  F  F\t\t T')
print('T  F  T\t\t T')
print('T  T  F\t\t F')
print('T  T  T\t\t T')

# Homework 3 Chapter 6

# 1. The four compass points can be abbreviated by single-letter strings as “N”, “E”, “S”, and “W”. Write a function
# turn_clockwise that takes one of these four compass points as its parameter, and returns the next compass point in
# the clockwise direction. Here are some tests that should pass:


# This program takes specific input from the user and prints out its correlating clockwise direction

user_input = input('Enter a capitalized compass point (N, E, S, W): ')


def turn_clockwise(c):
    """Compass Point Clock"""
    if c == 'N':
        print('E')
    elif c == 'E':
        print('S')
    elif c == 'S':
        print('W')
    elif c == 'W':
        print('N')
    else:
        print('None')


turn_clockwise(user_input)
# 7. Write a function to_secs that converts hours, minutes and seconds to a total number of seconds.

# The user inputs a number for hours, minutes, and secs which the function then returns the total number of seconds
Hours = float(input('Input hours: '))
Minutes = float(input('Input minutes: '))
Seconds = float(input('Input seconds: '))


def to_secs(h, m, s):
    hours = h * 3600
    minutes = m * 60
    seconds = s
    result = hours + minutes + seconds
    return print(result)


to_secs(Hours, Minutes, Seconds)

print(to_secs(2, 30, 10) == 9010)


# 10.Which of these tests fail? Explain why.

# I evaluated the following mathematical equations to test their accuracy.
# test(3 % 4 == 0)
print('Number 1 fails because 3 is not divisible by four. This should have a remainder of 3.')
# test(3 % 4 == 3)
print('Number 2 does not fail.')
# test(3 / 4 == 0)
print('Number 3 fails because the answer results in a decimal.')
# test(3 // 4 == 0)
print('Number 4 does not fail.')
# test(3+4  *  2 == 14)
print('Number 5 fails because using order of operations, the answer is 11.')
# test(4-2+2 == 0)
print('Number 6 fails because using order of operations, the answer is 4.')
# test(len("hello, world!") == 13)
print('Number 7 does not fail.')

