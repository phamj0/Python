# Chapter 8 Exercises


# 1
print('Question 1: ')

# printing result of problems
string = 'Python'
print(string[1])
sentence = 'Strings are sequences of characeters.'
print(sentence[5])
word = 'wonderful'
print(len(word))
word2 = 'Mystery'
print(word2[:4])
print('p' in 'Pineapple')
print('apple' in 'Pineapple')
print('pear' not in 'Pineapple')
print('apple' > 'pineapple')
print('pinapple' < 'Peach')

# 2
print('\nQuestion 2: ')
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter in ('O', 'Q'):
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)

# 3
print('\nQuestion 3: ')

def count_letters(fruit):
    count = 0
    for char in fruit:
        if char == "a":
         count += 1
    return count

fruit = 'banana'
print(count_letters(fruit))

def count_letters2(string, char, start):
    x = start
    while x < len(string):
        if string[x] == char:
            return x
        x += 1
    return -1

print(count_letters2(fruit, 'a', 0))