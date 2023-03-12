

# 9
def countVowels(string):
    vowels = 'AEIOUaeiou'
    count = 0
    for x in string:
        if x in vowels:
            count += 1
    return count

print(countVowels('My name is JAmie PhAm. I am twenty yEars Old'))


# 10
def numbers(sequence):
    list1 = []
    for x in str(sequence):
        if x not in list1:
            list1.append(x)
        else:
            return False
    return True

print(numbers(12345678))


#12
