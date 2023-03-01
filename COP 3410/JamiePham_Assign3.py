'''
Name: Jamie Pham
Date: February 28th 2023
Assignment #: 3

This assignment goes over Chapter 3 exercises.

'''

import matplotlib.pyplot as plt
import math

# R-3.1 

n = [10*x for x in range(1, 10)]

'''Graph 8n'''
x1 = n
y1 = []
for i in x1:
    y1.append(8*i)

'''Graph 4n log n'''
x2 = n
y2 = []
for i in x2:
    y2.append(4*i*math.log(i))

'''Graph 2n**2'''
x3 = n
y3 = []
for i in x3:
    y3.append(2*i**2)

'''Graph n**3'''
x4 = n
y4 = []
for i in x4:
    y4.append(i**3)

'''Graph 4n log n'''
x5 = n
y5 = []
for i in x5:
    y5.append(2**i)


plt.title('Question R-3.1')
plt.xlabel('n')
plt.ylabel('f(n)')


plt.xscale('log')
plt.yscale('log')

plt.scatter(x1, y1, color='blue')
plt.scatter(x2, y2, color='green')
plt.scatter(x3, y3, color='red')
plt.scatter(x4, y4, color='yellow')
plt.scatter(x5, y5, color='orange')

plt.show()

