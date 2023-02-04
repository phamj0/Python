
'''
Name: Jamie Pham
Date: January 29th 2023
Assignment #: 1

This assignment goes over Chapter 1 exercises.

'''

# R-1.1

print('Question 1: Finding multiples.\n')
mult1 = float(input('Enter an integer: '))
mult2 = float(input('Enter a second integer: '))

def is_multiple(n, m):
    if m % n == 0:      # using modulo function to find if there is a remainder
        return True
    else:
        return False

print(f'Is {mult1} a multiple of {mult2}? {is_multiple(mult1, mult2)}\n')

# R-1.3

print('Question 2: Finding Min and Max in a list.\n')
user_list = input('Enter 6 integers separated by spaces: ')

def minmax(k):
    sorted_list = sorted(k)     # sorted method sorts the input in ascending order
    return sorted_list[0], sorted_list[-1]      # returns the first and last integers in the list and returns it as a tuple

print(f'The min and max of the user inputted list are: {minmax(user_list.split())}.\n')

# R-1.4

print('Question 3: Finding the sum of sqaures of all positive integers smaller than the input.\n')
user_integer = int(input('Enter an integer: '))

def sumPositiveSquares(n):
    totalSum = 0        # initializing new variable that will contain the sum
    for x in range(1, n):
        totalSum += x ** 2      # adding each square in the range to variable one at a time
    return totalSum

print(f'The sum of the sqaures of all the positive integers smaller than {user_integer} is {sumPositiveSquares(user_integer)}.\n')

# R-1.5

print('Question 4: Finding the sum of sqaures of all positive integers smaller than the input part 2.\n')
user_integer = int(input('Enter an integer: '))

def sumPositiveSquares2(n):     # the problem calls for a single command but I inserted it into a function to be able to call it from the main function
     return sum(x ** 2 for x in range(1, n) if n > 0)     # one line command using comprehension syntax

print(f'The sum of the sqaures of all the positive integers smaller than {user_integer} is {sumPositiveSquares2(user_integer)}.\n')

# R-1.6

print('Question 5: Finding the sum of the squares of all odd positive integers smaller than the input.\n')
user_input = int(input('Enter an integer: '))

def sumOddSquares(n):
    sumOdd = 0      # initializing variable that will contain each square
    for x in range(1, n):
        if x % 2 == 1:      # finds if the number in the range is odd
            sumOdd += x ** 2
    return sumOdd

print(f'The sum of squares of the odd posotive integers smaller than {user_input} is {sumOddSquares(user_input)}.\n')

# R-1.7

print('Question 6: Finding the sum of the squares of all odd positive integers smaller than the input part 2.\n')
user_input = int(input('Enter an integer: '))

def sumOddSquares2(n):       # the problem calls for a single command but I inserted it into a function to be able to call it from the main function
    return sum(x**2 for x in range(1,n) if x % 2 == 1)      # one line command using comprehension syntax using sum function

print(f'The sum of squares of the odd posotive integers smaller than {user_input} is {sumOddSquares2(user_input)}.\n')

# R-1.9

def rangeConstructor():
    list1 = []      # creating an empty list
    for x in range(50, 81, 10):
        list1.append(x)     # appending each result to the empty list
    return list1


# R-1.10

def rangeConstructor2():
    list1 = []      # creating empty list
    for x in range(-8, 10, 2):
        list1.append(x)
    return list1[::-1]     # prints out resulting list but in reverse to match list given in the problem


# R-1.11

def listComp():
    return [2 ** x for x in range(9)]       # using list comprehension syntax, prints out the desired list


# main function that will call the last three problems at once

def main():
    print(f"Question 7: The parameters sent to the range constructor to produce the list {rangeConstructor()} is (50, 81, 10).")
    print(f"Question 8: The parameters sent to the range constructor to produce the list {rangeConstructor2()} is (-8, 10, 2).")
    print("Question 9: Using list comprehension syntax, I produced the following list: ", listComp())

main()
