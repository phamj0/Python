
# Chapter 3

for x in range(5):                                                              # 1
    print('I like turtles')

for x in ['January', 'February', 'March', 'April', 'May', 'June', 'July']:      # 2
    statement = 'The month is ' + x
    print(statement)

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]                                        # 5

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
