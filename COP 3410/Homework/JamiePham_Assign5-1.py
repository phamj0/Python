'''
Name: Jamie Pham
Date: April 8th 2023
Assignment #: 5

This assignment goes over Chapter 5 questions 1 and 2.

'''



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
            return self._data
        elif len(self._data) > 0:
            self._data.pop()
            return self.recursiveRemove()
        
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
    S = ArrayStack(5) # contents: [ ]
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
    print(len(S))
    print(S)
    S.push(1)
    print(S)
    S.recursiveRemove()
    print(S)
