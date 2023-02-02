
'''
Name: Jamie Pham
Date: January 29th 2023
Assignment #: 1

This assignment goes over Chapter 1 exercises.

'''

# R-1.1

def is_multiple(n, m):
    if m % n == 0:      # using modulo function to find if there is a remainder
        return True
    else:
        return False


# R-1.3

def minmax(k):
    sorted_list = sorted(k)     # sorted method sorts the input in ascending order
    return sorted_list[0], sorted_list[-1]      # returns the first and last integers in the list and returns it as a tuple

list = [5, 4, 6, 9, 2, 90]


# R-1.4

def sumPositiveSquares(n):
    totalSum = 0        # initializing new variable that will contain the sum
    for x in range(1, n):
        totalSum += x ** 2      # adding each square in the range to variable one at a time
    return totalSum


# R-1.5

def sumPositiveSquares2(n):     # the problem calls for a single command but I inserted it into a function to be able to call it from the main function
     return sum(x ** 2 for x in range(1, n) if n > 0)     # one line command using comprehension syntax


# R-1.6

def sumOddSquares(n):
    sumOdd = 0      # initializing variable that will contain each square
    for x in range(1, n):
        if x % 2 == 1:      # finds if the number in the range is odd
            sumOdd += x ** 2
    return sumOdd


# R-1.7

def sumOddSquares2(n):       # the problem calls for a single command but I inserted it into a function to be able to call it from the main function
    return sum(x**2 for x in range(1,n) if x % 2 == 1)      # one line command using comprehension syntax using sum function


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


# main function that will call each problem at once

def main():
    print("Is 12 a multiple of 60?", is_multiple(12, 60))
    print("From the given list, the min and max of the list are: ", minmax(list))
    print("The sum of the squares of all the positive integers smaller than 5 is: ", sumPositiveSquares(5))
    print("Using comprehension syntax for the previous problem, the answer is: ", sumPositiveSquares2(5))
    print("The sum of the squares of all the odd positive integers smaller than 6 is: ", sumOddSquares(6))
    print("Using comprehension syntax for the previous problem, the answer is: ", sumOddSquares2(6))
    print(f"The parameters sent to the range constructor to produce the list {rangeConstructor()} is (50, 81, 10).")
    print(f"The parameters sent to the range constructor to produce the list {rangeConstructor2()} is (-8, 10, 2).")
    print("Using list comprehension syntax, I produced the following list: ", listComp())

main()
