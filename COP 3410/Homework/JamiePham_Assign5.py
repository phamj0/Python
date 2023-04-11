'''
Name: Jamie Pham
Date: April 8th 2023
Assignment #: 5

This assignment goes over Chapter 5 questions.

'''



class ArrayStack:
    '''LIFO Stack implementation using a Python list as underlying storage.'''

    def __init__ (self, maxlen = 5):
        '''Create an empty stack.'''
        self._maxlen = maxlen
        self._data = [None] * maxlen               
        
    def __len__ (self):
        '''Return the number of elements in the stack.'''
        return len(self._data)

    def is_empty(self):
        '''Return True if the stack is empty.'''
        return len(self._data) == 0

    def push(self, e):
        '''Add element e to the top of the stack.'''
        if self._data[0] == None:
            self._data.pop(0)
            self._data.append(e)
        elif self._data[-1] == None:
            self._data.pop(-1)
            self._data.append(e)
        elif self._data[0] != None or self._data[-1] != None:
            raise Exception('Can not push element. Maximum Capacity reached.')

    def top(self):
        '''Return (but do not remove) the element at the top of the stack.
         Raise Empty exception if the stack is empty.
         '''
        if self.is_empty( ):
             raise Empty( 'Stack is empty' )
        return self._data[-1]          # the last item in the list

    def pop(self):
        '''Remove and return the element from the top of the stack (i.e., LIFO).
         Raise Empty exception if the stack is empty.
        '''
        if self.is_empty( ):
          raise Empty( 'Stack is empty' )
        else:
            self._data.pop()
            self._data.append(None)

    def recursiveRemove(self):
        '''Method for removing all elements in the stack'''
        if len(self._data) == 0:
            self._data = [None] * self._maxlen
            return self._data
        elif len(self._data) > 0:
            self._data.pop()
            return self.recursiveRemove()
        
    def driver(self):
        '''Driver function to test changes made to class'''
        self.push(7)
        self.push(7)
        self.push(7)
        self.push(7)
        self.push(7)
        self.pop()
        self.push(7)
        # self.push(7)      # Adds 6th element which exceeds capacity of 5 to raise error
        self.recursiveRemove()
        return self

    def __str__(self):
        '''Returns string of list object'''
        return str(self._data)


class Empty(Exception):       # Defines an Empty class as a trivial subclass of the Python Exception class.
    '''Error attempting to access an element from an empty container.'''
    pass

def reverse_file(filename):
    '''Overwrite given file with its contents line-by-line reversed.'''
    print("reversefile executing")
    S = ArrayStack()
    original = open(filename)
    for line in original:
        for i in line:
            S.push(i) # we will re-insert newlines when writing
    original.close( )
    # now we overwrite with contents in LIFO order
    output = open(filename, 'w' ) # reopening file overwrites original
    while not S.is_empty( ):
        output.write(S.pop( )) # re-insert newline characters
    output.close( )


if __name__ == "__main__": 
    S = ArrayStack( ) # contents: [ ]
    print(len(S))
    print(S)
    S.push(5)
    print(S)
    S.push(4)
    print(S)
    S.push(3)
    print(S)
    S.push(2)
    print(S)
    S.push(1)
    print(S)
    S.pop()
    print(S)
    S.push(1)
    print(S)
    S.recursiveRemove()
    print(S)

    newStack = ArrayStack()
    print(newStack.driver())
    

    
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

# There should be a total of 22 elements left in the queue. 