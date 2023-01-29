
prompt = input('Please enter a string of characters: ')

def findX(string):
    index = string.lower().find('x')
    count = 0
    for x in string.lower():
        if x == 'x':
            count += 1
    print('The first character x is found at index', index)
    print('There is a total of', count, 'x\'s in the string entered')
    


findX(prompt)
