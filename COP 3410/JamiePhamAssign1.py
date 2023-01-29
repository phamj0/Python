
'''
Name: Jamie Pham
Date: January 29th 2023
Assignment #: 1

This assignment goes over Chapter 1 exercises.

'''

# R-1.1

def is_multiple(n, m):
    if m % n == 0:
        return True
    else:
        return False

print(is_multiple(12, 60))

# R-2.3

def minmax(k):
    sorted_list = sorted(k)
    return sorted_list[0], sorted_list[-1]

list = [5, 4, 6, 9, 2, 90]
print(minmax(list))

# R-1.4

def sumPositiveSquares(n):
    totalSum = 0
    for x in range(1, n+1):
        totalSum += x ** 2
    return totalSum

print(sumPositiveSquares(4))

# R-1.5

def sumPositiveSquaresPart2(n):
     return sum(x ** 2 for x in range(1, n+1) if n > 0)

print(sumPositiveSquaresPart2(4))