
class ArrayStack:
    '''LIFO Stack implementation using a Python list as underlying storage.'''

    def __init__ (self, maxlen = 50):
        '''Create an empty stack.'''
        self._maxlen = maxlen
        self._data = [None] * maxlen               
        
    def __len__ (self):
        '''Return the number of elements in the stack.'''
        count = 0
        for i in self._data:
            if i != None:
                count += 1
        return count

    def is_empty(self):
        '''Return True if the stack is empty.'''
        return len(self._data) == 0

    def push(self, e):
        '''Add element e to the top of the stack.'''
        if self._data[0] == None:
            self._data.pop(0)
            self._data.append(e)
        elif len(self._data) < self._maxlen:
            self._data.append(e)
        elif self._data[0] != None or len(self._data) == self._maxlen:
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

    def recursiveRemove(self):
        '''Method for removing all elements in the stack'''
        if len(self._data) == 0:
            self._data = [None] * self._maxlen
            return self._data
        elif len(self._data) > 0:
            self._data.pop()
            return self.recursiveRemove()
        
    def __str__(self):
        '''Returns string of list object'''
        filtered_str = []
        for i in self._data:
            if i != None:
                filtered_str.append(i)
        return str(filtered_str)


class Empty(Exception):       # Defines an Empty class as a trivial subclass of the Python Exception class.
    '''Error attempting to access an element from an empty container.'''
    pass

###############################################################################################

class Queue(object):
   def __init__(self, size=50):             # Constructor
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
 
   def is_empty(self): 
      return self.__nItems == 0
 
   def is_full(self): 
      return self.__nItems == self.__maxSize
 
   def __len__(self): 
      return self.__nItems
 
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

if __name__ == '__main__':

# 6.3 

# Implement a function with signature transfer(S, T) that transfers all elements from stack S onto stack T, 
# so that the element that starts at the top of S is the first to be inserted onto T,
# and the element at the bottom of S ends up at the top of T.

    def transfer(S, T):
        while len(S) > 0: 
            T.push(S.top())
            S.pop()
        return T

    listS = ArrayStack()
    listS.push(10)
    listS.push(9)
    listS.push(8)
    listS.push(7)
    listS.push(6)
    print(listS)
    
    listT = ArrayStack()
    listT.push(1)
    listT.push(2)
    listT.push(3)
    listT.push(4)
    listT.push(5)
    print(listT)

    print(transfer(listS, listT))

# 6.4 

# Give a recursive method for removing all the elements from a stack.

    def remove(stack):
        if len(stack) == 0:
            return stack
        else:
            stack.pop()
            remove(stack)
        

    newStack = ArrayStack()

    newStack.push(1)
    newStack.push(1)
    newStack.push(1)
    newStack.push(1)
    newStack.push(1)
    newStack.push(1)
    newStack.push(1)
    # print(newStack)

    # print(remove(newStack))


# 6.5

# Implement a function that reverses a list of elements by pushing them onto
# a stack in one order, and writing them back to the list in reversed order.

    def reverse(List, subStack):
        for item in List:
            subStack.push(item)
        List.clear()
        while len(subStack) > 0:
            List.append(subStack.top())
            subStack.pop()
        return List
        

    emptyStack = ArrayStack()

    initialList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # print(reverse(initialList, emptyStack))


# 6.13

# Suppose you have a deque D containing the numbers (1,2,3,4,5,6,7,8),
# in this order. Suppose further that you have an initially empty queue Q.
# Give a code fragment that uses only D and Q (and no other variables) and
# results in D storing the elements in the order (1,2,3,5,4,6,7,8).
    from collections import deque

    D = deque([1, 2, 3, 4, 5, 6, 7, 8])
    Q = Queue()

    for x in D:
        Q.enqueue(x)
    print(Q)
    

# 6-14

# Repeat the previous problem using the deque D and an initially empty stack S.
    
    D = deque([1, 2, 3, 4, 5, 6, 7, 8])
    S = ArrayStack()

    for x in D:
        S.push(x)
    print(S)