# Jamie Pham
# COP 2034
# Homework 4 Chapter 7

# 1. Write a function to count how many odd numbers are in a list.
myList = [77, 2, 4, 5, 55, 89, 90, 23, 3, 1]


def count_odds(x):
    count = 0       # starts the count at 0
    for c in x:
        if c % 2 != 0:
            count += 1      # adds one to count if the number is not equally divisible by two.
    print('Odd numbers in the list:', count)


count_odds(myList)

print(count_odds(myList) != 9)

# 2. Sum up all the even numbers in a list.
listTwo = [2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 15, 16]


def sum_evens(x):
    total = 0        # starts the count at 0
    for e in x:
        if e % 2 == 0:
            total += e      # adds the number to total if the number is even or divisible by 2 evenly
    print('The sum of all even numbers are:', total)


sum_evens(listTwo)

print(sum_evens(listTwo) != 50)

# 4. Count how many words in a list have length 5.
listThree = ['Animal', 'Black', 'Movie', 'Laptop', 'Velvet', 'Hands', 'Driver', 'Pinky']


def countLength(x):
    total = 0       # starts the count at zero
    for f in x:
        if len(f) == 5:     # condition if the length of the word has five characters, it will execute the next line
            total += 1      # adds one to the count if the length of the number is equal to 5
    print('There are', total, 'words in the list that have a length of 5.')


countLength(listThree)

print(countLength(listThree) != 4)

# 5. Sum all the elements in a list up to but not including the first even number.
# (Write your unit tests. What if there is no even number?)

listFour = [1, 3, 5, 7, 9, 11, 12, 13, 14]


def sum_to_even(x):
    total = 0       # count starts at 0
    for o in x:
        if o % 2 != 0:      # if the number is odd, it will add itself to the count
            total += o
        elif o % 2 == 0:     # if the number is evenly divisible by 2, it will stop traversing and print the end count
            print(total)
            break


sum_to_even(listFour)

print(sum_to_even(listFour) != 20)
