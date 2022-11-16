
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
def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print(better)
        if abs(approx - better) < 0.001:
            return better
        approx = better

print(sqrt(25), '\n')


# 8
print('Question 8: ')
def print_multiples(n, high):
    for i in range(1, high+1):
        print(n * i, end="   ")
    print()

def print_mult_table(high):
    for i in range(1, high+1):
        print_multiples(i, high)

print(print_mult_table(5), '\n')


# 9
print('Question 9: ')
def print_triangular_numbers(n):
    for x in range(1, n+1):
        print(x, x*(x+1)/2)

print(print_triangular_numbers(5), '\n')


# 10
print('Question 10: ')
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
               return False
        return True

print(is_prime(19), '\n')


# 14
print('Question 14: ')
def num_digits(n):
    count = 0
    if n == 0:
        return 1
    while n != 0:
        count = count + 1
        n = n // 10
    return count

print(num_digits(100), '\n')

