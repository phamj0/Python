
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
        return 'None\n'

user_input = str(input('Enter a month to return amount of days: '))

print('There are', days_in_month(user_input), f'days in {user_input}.\n')


# 7 and 8
print('Question 7 and 8: ')
def to_secs(x, y, z):
    h = x * 60 * 60
    m = y * 60
    s = z
    total_secs = int(h+m+s)
    print('Given input =', total_secs, 'seconds in total.\n')

hours = float(input('Enter number of hours: '))
minutes = float(input('Enter number of minutes: '))
seconds = float(input('Enter number of seconds: '))

to_secs(hours, minutes, seconds)


# 9
print('Question 9: ')
