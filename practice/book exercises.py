
# Chapter 3

for x in range(5):                                                              # 1
    print('I like turtles')

for x in ['January', 'February', 'March', 'April', 'May', 'June', 'July']:      # 2
    statement = 'The month is ' + x
    print(statement)

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]                                        # 5

for x in xs:
    print(x)

for x in xs:
    print(x, x**2)

total = 0
for x in xs:
    total += x
print(total)

total = 1
for x in xs:
    total *= x
print(total)

# Chapter 5


def weekDays(x):                                                                # 1
    if x == 0:
        print('Sunday')
    elif x == 1:
        print('Monday')
    elif x == 2:
        print('Tuesday')
    elif x == 3:
        print('Wednesday')
    elif x == 4:
        print('Thursday')
    elif x == 5:
        print('Friday')
    elif x == 6:
        print('Saturday')
    else:
        print('Invalid choice.')


user_input = float(input('Enter a number from 0 - 6: '))

weekDays(user_input)

weekDays = {0: 'Sunday',                                                         # 2
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday'}

departure = int(input('What is the day of departure 0 - 6? '))
duration = int(input('What is the duration of stay? '))
x = (duration + departure) % 7

print('You will return on', weekDays[x])


def grade(x):                                                                    # 6
    if x >= 75:
        print('First')
    elif x >= 70:
        print('Upper Second')
    elif x >= 60:
        print('Second')
    elif x >= 50:
        print('Third')
    elif x >= 45:
        print('F1 Supp')
    elif x >= 40:
        print('F2')
    elif x < 40:
        print('F3')


# studentGrade = int(input('Enter your grade: '))

# grade(studentGrade)

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for z in xs:
    print('Mark: ' + str(z) + ' Grade: ', end=''), (grade(z))


def find_hypo(x, y):                                                          # 10
    hypotenuse = (x**2 + y**2)**0.5
    rounded = round(hypotenuse, 2)
    print('The hypotenuse is: ', rounded)


xx = float(input('First side: '))
yy = float(input('Second side: '))
find_hypo(xx, yy)


def is_right(x, y, z):                                                          # 11
    answer = x**2 + y**2
    if answer != z**2:
        print('False')
    elif answer == z**2:
        print('True')


sideA = float(input('Length of first side: '))
sideB = float(input('Length of second side: '))
sideC = float(input('Length of third side: '))

is_right(sideA, sideB, sideC)

