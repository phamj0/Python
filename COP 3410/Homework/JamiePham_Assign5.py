



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


class Empty(Exception):                 # Defines an Empty class as a trivial subclass of the Python Exception class.
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
    

    






