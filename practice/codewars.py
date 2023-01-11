'''Finding the work witht he highest score according to the letters position in the alphabet'''

def high(x):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    word = x.split()
    for x in word:
       for i in x:
            alp.find(i) + 1