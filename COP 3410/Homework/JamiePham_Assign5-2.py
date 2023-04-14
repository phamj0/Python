'''
Name: Jamie Pham
Date: April 8th 2023
Assignment #: 5

This assignment goes over Chapter 5 questions 3 and 4.

'''
##########################Queue Class##########################

# Implement a Queue data structure using a Python list

class Queue(object):
   def __init__(self, size):             # Constructor
      self.__maxSize = size              # Size of [circular] array
      self.__que = [None] * size         # Queue stored as a list
      self.__front = 1                   # Empty Queue has front 1
      self.__rear = 0                    # after rear and
      self.__nItems = 0                  # No items in queue
 
   def enqueue(self, item):               # Insert item at rear of queue
      if self.is_full():                  # if not full
         raise Exception("Queue overflow")
      self.__rear += 1                   # Rear moves one to the right
      if self.__rear == self.__maxSize:  # Wrap around circular array
         self.__rear = 0
      self.__que[self.__rear] = item     # Store item at rear
      self.__nItems += 1
      return True
 
   def dequeue(self):                     # Remove front item of queue
      if self.is_empty():                 # and return it, if not empty
         raise Exception("Queue underflow")
      front = self.__que[self.__front]   # get the value at front
      self.__que[self.__front] = None    # Remove item reference
      self.__front += 1                  # front moves one to the right
      if self.__front == self.__maxSize: # Wrap around circular arr.
         self.__front = 0
      self.__nItems -= 1
      return front
 
   def first(self):                       # Return frontmost item
      return None if self.is_empty() else self.__que[self.__front]
 
   def is_empty(self): return self.__nItems == 0
 
   def is_full(self): return self.__nItems == self.__maxSize
 
   def __len__(self): return self.__nItems
 
   def __str__(self):                    # Convert queue to string
      ans = "["                          # Start with left bracket
      for i in range(self.__nItems):     # Loop through current items
         if len(ans) > 1:                # Except next to left bracket,
            ans += ", "                  # separate items with comma
         j = i + self.__front            # Offset from front
         if j >= self.__maxSize:         # Wrap around circular array
            j -= self.__maxSize
         ans += str(self.__que[j])       # Add string form of item
      ans += "]"                         # Close with right bracket
      return ans

if __name__ == "__main__":
    Q = Queue(20)    #create an object of array queue
    Q.enqueue(5)
    print(Q)
    Q.enqueue(3)
    print(Q)
    Q.dequeue()
    print(Q)
    Q.enqueue(2)
    print(Q)
    Q.enqueue(8)
    print(Q)
    Q.dequeue()
    print(Q)
    Q.dequeue()
    print(Q)
    Q.enqueue(9)
    print(Q)
    Q.enqueue(1)
    print(Q)
    Q.dequeue()
    print(Q)
    Q.enqueue(7)
    print(Q)
    Q.enqueue(6)
    print(Q)
    Q.dequeue()
    print(Q)
    Q.dequeue()
    print(Q)
    Q.enqueue(4)
    print(Q)
    Q.dequeue()
    print(Q)
    Q.dequeue()
    print(Q)        # answer to question 3


# Question 4

# Out of the 32 enqueues, 15, dequeues, and 10 first operations, the first operations
# do not affect the elements in the queue and only returns them. Therefore, I rule out the first operations.
# Starting with an empty list and performing 32 enqueues, there should be 32 elements currently.
# Out of the 15 dequeues, 5 failed. Subtracting 10 dequeues from 32 enqueues results in 22.
# In conclusion, here should be a total of 22 elements left in the queue. 