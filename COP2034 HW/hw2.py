# Homework 2 Chapter 4

# 7.

n_input = int(input('Enter an integer for its summation: '))


def sum_to(n):
    """Creating an interactive summation program"""
    # the variable total starts the summation at 0
    total = 0
    for n in range(1, n + 1):
        # the add and assign operand allows the total variable to continuously add and reassign the value to the
        # variable
        total += n
    return total


print(sum_to(n_input))


# 8. Write a function area_of_circle(r) which returns the area of a circle of radius r.

def area_of_circle(n):
    area = (3.14 * radius ** 2)
    print('The area is', area)

radius = float(input('Enter a number for the radius: '))

area_of_circle(radius)


# Homework 2 Chapter 5

# 1. Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write a function which is given
# the day number, and it returns the day name (a string).

# First assign each day to a number
def number_to_day(n):
    """Converting a number to a weekday"""
    if n == 0:
        print("sunday")
    elif n == 1:
        print('monday')
    elif n == 2:
        print('tuesday')
    elif n == 3:
        print('wednesday')
    elif n == 4:
        print('thursday')
    elif n == 5:
        print('friday')
    elif n == 6:
        print('saturday')
    else:
        print('Number is not an integer or within the given range')


user_input = float(input('Enter an integer in range 0-6: '))
number_to_day(user_input)

# 3. Give the logical opposites of these conditions

# a > b
print('The logical opposite od a > b a <= b')
# a >= b
print('The logical opposite of a >= b is a < b')
# a >= 18  and  day == 3
print('The logical opposite of a >= 18  and  day == 3 is a < 18 and day != 3')
# a >= 18  and  day != 3
print('The logical opposite of a >= 18  and  day != 3 is a < 18 and day == 3')

# 4. What do these expressions evaluate to?

# 3 == 3
print('3==3 evaluates to true')
# 3 != 3
print('3 != 3 evaluates to false')
# 3 >= 4
print('3 >= 4 evaluates to false')
# not (3 < 4)
print('3 < 4 evaluates to false')
