
# Chapter 3 Exercises

# 1
for x in range(5):
    print('I like turtles')


# 2
for x in ['January', 'February', 'March', 'April', 'May', 'June', 'July']:      
    statement = 'The month is ' + x
    print(statement)


# 5
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]                                        

for x in xs:
    print(x)

for x in xs:
    print(x, x**2)

total = 0
for x in xs:
    total += x
print(total)

total = 1
for x in xs:
    total *= x
print(total)
