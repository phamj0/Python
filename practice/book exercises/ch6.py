
# Chapter 6 Exercises

# 1
print('Question 1: ')
def turn_clockwise(x):                                                      
    if x == 'N':
        return 'E'
    elif x == 'E':
        return 'S'
    elif x == 'S':
        return 'W'
    elif x == 'W':
        return 'N'
    else:
        return 'None'

user_input = input('Enter a compass point: ')

print('The clockwise compass point is:', turn_clockwise(user_input), '\n')

#test
# print(turn_clockwise('N')== 'E')


# 2
print('Question 2: ')
daysOftheWeek = {0: 'Sunday',
                 1: 'Monday',
                 2: 'Tuesday',
                 3: 'Wednesday',
                 4: 'Thursday',
                 5: 'Friday',
                 6: 'Saturday'}

def day_name(x):
    if x < 7:
        return daysOftheWeek[x]
    elif x > 6:
        return 'None'
    else:
        return 'Not an integer'

given_number = int(input('Enter an interger in range 0 - 6 to return a day of the week: '))

print(f'Day number {given_number} is', day_name(given_number), '\n')


# 3
print('Question 3: ')
def day_num(x):
    week_days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    if x not in week_days:
        return 'None'
    else:
        return week_days.index(x)
    
user_answer = str(input('Enter a capitalized weekday: '))

print(f'{user_answer} is day number', day_num(user_answer), '\n')


# 4 and 5
print('Question 4 and 5: ')
def day_add(x, y):
    week_days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    if x in week_days:
        dayLeft = week_days.index(x)
        daysGone = dayLeft + y
        returnDay = daysGone % 7
        print('You will return on a', week_days[returnDay], '\n')
    else:
        print('Error\n')


A = str(input('What day do you leave for vacation? '))
B = int(input('How many days will you be gone? '))

day_add(A, B)

# The function above also works with negative input because the final integer
# will work as a negative index.


# 6
print('Question 6: ')

month_days = {'January': 31,
              'February': 28,
              'March': 31,
              'April': 30,
              'May': 31,
              'June': 30,
              'July': 31,
              'August': 31,
              'September': 30,
              'October': 31,
              'November': 30,
              'December': 31}

def days_in_month(x):
    if x in month_days:
        return month_days[x]
    else:
        return 'None'

user_input = str(input('Enter a month to return amount of days: '))

print('There are', days_in_month(user_input),f'days in {user_input}.\n')


# 7 and 8
print('Question 7 and 8: ')
def to_secs(x, y, z):
    h = x * 60 * 60
    m = y * 60
    s = z
    total_secs = int(h+m+s)
    print(f'Given input = {total_secs} seconds in total.\n')

hours = float(input('Enter number of hours: '))
minutes = float(input('Enter number of minutes: '))
seconds = float(input('Enter number of seconds: '))

to_secs(hours, minutes, seconds)


# 9
print('Question 9: ')
def hours_in(x):
    if x >= 3600:
        return round(x // 3600)
    elif x < 3600:
        return 'Not enough seconds for an hour.'

user_hours = float(input('Enter number of seconds to convert to whole hours: '))

print(hours_in(user_hours),'\n')


def minutes_in(x):
    if x >= 3600:
        new_total = x % 3600
        total = new_total // 60
        return round(total)
    elif x >= 60:
        return round(x // 60)
    else:
        return 'Not enough seconds for a minute.'

user_minutes = float(input('Enter a number of seconds to convert to remaining minutes: '))

print(minutes_in(user_minutes), '\n')


def seconds_in(x):
    if x >= 3600:
        a = x % 3600
        b = a % 60
        first_total = b % 60
        return round(first_total)
    elif x >= 60:
        c = x % 60
        return round(c)
    elif x < 60:
        return round(x)
    else:
        return 'None'

user_seconds = float(input('Enter a number of seconds to get remaining seconds: '))

print(seconds_in(user_seconds), '\n')


# 11
print('Question 11: ')
def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 'None'

a_compare = int(input('Enter your first integer: '))
b_compare = int(input('Enter a second integer: '))

print(compare(a_compare, b_compare), '\n')


# 12
print('Question 12: ')
def hypotenuse(a, b):
    c = a**2 + b**2
    length = c ** 0.5
    return round(length, 1)

sideA = int(input('Enter a side length: '))
sideB = int(input('Enter a second side length: '))

print(hypotenuse(sideA, sideB), '\n')


# 13
print('Question 13: ')
def slope(x1, y1, x2, y2):
    y = y2 - y1
    x = x2 - x1
    m = y / x
    return m
    
x1_coordinate = int(input('Enter integer: '))
x2_coordinate = int(input('Enter integer: '))
y1_coordinate = int(input('Enter integer: '))
y2_coordinate = int(input('Enter integer: '))

print(slope(x1_coordinate, x2_coordinate, y1_coordinate, y2_coordinate), '\n')


# 14
print('Question 14: ')
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

user_even = int(input('Enter an integer for even boolean: '))

print(is_even(user_even), '\n')


# 15
print('Question 15: ')
def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False

user_odd = int(input('Enter an integer for odd boolean: '))

print(is_odd(user_odd), '\n')


# 16
print('Question 16: ')
def is_factor(f, n):
    if n % f == 0:
        return True
    else:
        return False

factor_a = int(input('Enter a number: '))
factor_b = int(input('Enter a number: '))

print(is_factor(factor_a, factor_b), '\n')


# 17
print('Question 17: ')
def is_multiple(m, n):
    if m % n == 0:
        return True
    else:
        return False

multipleOne = int(input('Enter a number: '))
multipleTwo = int(input('Enter a number: '))

print(is_multiple(multipleOne, multipleTwo), '\n')


# 18
print('Question 18:')
def f2c(f):
    c = (f - 32) * 5/9
    return round(c)

fahrenheit = int(input('Enter degrees in Fahrenheit to convert to Celsius: '))

print(f2c(fahrenheit), '\n')


# 19
print('Question 19: ')
def c2f(c):
    f = (c * 9/5) + 32
    return round(f)

celsius = int(input('Enter degrees in Celsius to convert to Fahrenheit: '))

print(c2f(celsius), '\n')
