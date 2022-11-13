
# Chapter 7 Exercises


# 1
print('Question 1: ')
def count_odd():
    listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = 0
    for x in listA:
        if x % 2 == 1:
            count +=1
    return count

print(f'There are {count_odd()} odd numbers in the list.\n')


#2
print('Question 2: ')
def sum_even():
    listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = 0
    for x in listA:
        if x % 2 == 0:
            count += x
    return count

print(f'The total sum of all even numbers in the list is {sum_even()}.\n')


# 3
print('Question 3: ')
def sum_negative():
    listB = [1, -6, 4, -77, - 33, -1, 3, 6]
    total = 0
    for x in listB:
        if x < 0:
            total += x
    return total

print(f'The sum of all negative number in the list is {sum_negative()}.\n')


# 4
print('Question 4: ')
def len_five():
    listC = ['Tomato', 'Avocado', 'Woman', 'Water', 'Cooler']
    count = 0
    for x in listC:
        if len(x) == 5:
            count += 1
    return count

print(f'There are {len_five()} word(s) with a length of five in the list.\n')


# 5
print('Question 5: ')
def first_even():
    listD = [3, 5, 7, 9, 13, 15, 6, 14, 17, 19]
    total = 0
    for x in listD:
        if x % 2 == 1:
            total += x
        elif x % 2 == 0:
            break
    return total

print(f'The sum of odd numbers before the first even number is {first_even()}.\n')


# 6
print('Question 6: ')
def count_words():
    listE = ['Tomato', 'Avocado', 'Woman', 'Water', 'Cooler', 'Sam', 'Jamie']
    count = 0
    for x in listE:
        if x == 'Sam':
            break
        else:
            count += 1
    return count

print(f'There are {count_words()} words before Sam appears in the list.\n')


# 7
print('Question 7: ')

def