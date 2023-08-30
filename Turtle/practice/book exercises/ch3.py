
# Chapter 3 Exercises

# 1
print('Question 1: ')
for x in range(5):
    print('I like turtles')

print('\n')

# 2
print('Question 2: ')
for x in ['January', 'February', 'March', 'April', 'May', 'June', 'July']:      
    statement = 'The month is ' + x
    print(statement)

print('\n')

# 5
print('Question 5: ')
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]                                        

for x in xs:
    print(x)
print('\n')

for x in xs:
    print(x, x**2)
print('\n')

total = 0
for x in xs:
    total += x
print(total)
print('\n')

total = 1
for x in xs:
    total *= x
print(total)
print('\n')
