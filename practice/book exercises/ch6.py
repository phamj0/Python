
# Chapter 6 Exercises

# 1
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

print('The clockwise compass point is:', turn_clockwise(user_input))

#test
# print(turn_clockwise('N')== 'E')


# 2
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

given_number = int(input('\nEnter an interger in range 0 - 6 to return a day of the week: '))

print(f'Day number {given_number} is', day_name(given_number))


# 3
def day_num(x):
    week_days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    if x not in week_days:
        return 'None'
    else:
        return week_days.index(x)
    
user_answer = str(input('\nEnter a capitalized weekday: '))

print(f'{user_answer} is day number', day_num(user_answer))


# 4
def day_add(x, y):
    week_days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    dayLeft = week_days.index(x)
    daysGone = dayLeft + y
    returnDay = daysGone % 7
    print('\nYou will return on a', week_days[returnDay])

A = str(input('\nWhat day do you leave for vacation? '))
B = int(input('\nHow many days will you be gone? '))

day_add(A, B)


