
from time import time
import matplotlib.pyplot as plt

input_size = []   #x axis
running_time = []  # y axis

for i in range(50,500,200):
    start_time = time( ) # record the starting time


    
    input_size.append(i**2)
    data = [k for k in range(i**2)]

    #algorithm design any algorithm
    
    def selection_sort(A):
        '''
        sort by ascending order
        '''


        for i in range(1,len(A)):     #outer loop goes through the list
            for j in range(i,0,-1):   #inner loop moves to the left of the current value
                if A[j] < A[j-1]:     #Swap two values if out of order
                    temp = A[j]
                    A[j] = A[j-1]
                    A[j-1] = temp
        return A; 
    
    print(selection_sort(data))
    
    end_time = time( ) # record the ending time
    elapsed = end_time - start_time # compute the elapsed time

    
    running_time.append(elapsed * 1e3)

plt.scatter(input_size, running_time)
#plt.plot(input_size, running_time, marker='o')
plt.show()




