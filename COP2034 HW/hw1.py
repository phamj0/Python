# Homework 1 Chapter 2

# 1. Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, then print
# out the sentence on one line using print.

w1 = 'All'
w2 = 'work'
w3 = 'and'
w4 = 'no'
w5 = 'play'
w6 = 'makes'
w7 = 'Jack'
w8 = 'a'
w9 = 'dull'
w10 = 'boy'

print(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10)

# 5. Write a Python program that assigns the principal amount of $10000 to variable P, assign to n the value 12,
# and assign to r the interest rate of 8%. Then have the program prompt the user for the number of years t that the
# money will be compounded for. Calculate and print the final amount after t years.

p = 10000
n = 12
r = 0.08

print('How many years (t) will the money be compounded for? ')
t = int(input('Years: '))

total_amount = p * ((1 + r / n) ** (n * t))

print(total_amount)

# 6. What happened with the last example? Why? If you were able to correctly anticipate the computer’s response in
# all but the last one, it is time to move on. If not, take time now to make up examples of your own. Explore the
# modulus operator until you are confident you understand how it works.
a = 5 % 2
b = 9 % 5
c = 15 % 12
d = 12 % 15
e = 6 % 6
f = 0 % 7
print(a, b, c, d, e, f)
# g = 7 % 0
# The equation above is a comment because running the program with it caused an error that didn't allow me to
# continue running the rest of the program
# I was able to correctly anticipate all the answers. The last example resulted in an error because nothing is
# divisible by zero

# 7. You look at the clock, and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm
# go off?
hr_24 = (51 % 24)+14
hr_12 = (hr_24 - 12)
print(hr_12)
