# Name: Jamie Pham
# Date: Jan 10, 2023
# Assignment 0 



def evenOdd():
    listA = [4, 7, 98, 34, 2, 14, 15, 10, -30, 8.9]
    for x in listA:
        if x % 2 == 0:
            print(str(x) + ' is even')
        elif x % 2 == 1:
            print(str(x) + ' is odd')
        else:
            print(str(x) + ' is not an integer.')

evenOdd()