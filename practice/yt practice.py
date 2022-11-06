# the following lines shows what you can do with strings

print('Jamie Pham')  # prints out the string onto the console

name = 'Jamie Pham'  # declared variable with value jamie pham
print(name[4])  # prints out the fourth letter of the string
print(name.index('e'))  # index of the string begins with zero.
# This will print the number 4
print(name.replace('Pham', 'Pinto'))  # just replaces the two phrases

# the following lines show what you can do with numbers

print(-2.0987)  # can print numbers without quotation marks
print(3 + 5)  # obviously python can do math (PEMDAS)
print(3 + 7 * 2)

my_num = 7
print(my_num)  # just prints the variable 7

print(str(my_num))  # converts the number into a string

print(my_num, 'is my favorite number.')
# print(my_num + 'is my favorite number')
# the line above shows that you cannot concatenate a number with a string
print(str(my_num) + ' is my favorite number.')  # str + str. this works

my_num1 = -10
print(abs(my_num1))  # function stands for absolute value. prints 10
print(pow(3, 2))  # function is power or exponentiation. answer is 9
print(pow(3, 8))
print(max(1, 9))  # min and max function prints the number that is
print(min(4, 1))  # lowest (min) or highest (max)
print(round(2.56789))  # just rounds the number

from math import *

# line above gives access to more math functions in python

print(floor(4.9))  # rounds down to the nearest whole number. prints 4
print(ceil(4.1))  # opposite of floor. rounds up. prints 5
print(sqrt(81))  # just square roots. prints 9

# the following is getting input from user

name = input('Enter your name: ')
age = input('Enter your age: ')
print('Hello ' + name + '! You are ' + age + '.')

num1 = float(input('enter number 1: '))
num2 = input('enter number 2: ')

result = num1 + float(num2)  # remember float is for decimal numbers

print(result)

# lists

hunter_friends = ['Hisoka', 'Killua', 'Gon', 'Bisky']

print(hunter_friends)

# tuples

colors = ('pink', 'blue', 'yellow')

print(colors[0])

# dictionaries

word_bank ={
    'jam': 'Jamie',
    'felip': 'Felipe',
    'mom': 'Kathy',
}

print(word_bank['mom'])


