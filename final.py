string1 = "China is one of the fastest-growing economies in the world. China is looking for more investments around the world. Also, the whole world is looking at China as a great economic power. Most of the Chinese can foresee the heights that China is capable of reaching."

def num13(x):    
    countThe = 0
    y = x.split()
    for z in y:   
     if z == 'the':
        countThe += 1
    longest = max(string1.split(), key=len)
    return longest, countThe

print(num13(string1))
    





