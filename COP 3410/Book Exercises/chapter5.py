# 1
'''
import sys
data = []
for k in range(27):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}: Size in bytes: {1:4d}'.format(a, b))
    data.append(None)
'''

# 2
'''
import sys  

data = []
for k in range(30):  
    a = len(data) 
    b = sys.getsizeof(data)
    data.append(k)
    c = sys.getsizeof(data)
    if b != c:
        print(k)
'''

# 4

import ctypes 

class DynamicArray:
    '''A dynamic array class akin to a simplified Python list.'''

    def __init__ (self):
        '''Create an empty array'''
        self._n=0 
        self._capacity = 1 
        self._A = self._make_array(self._capacity) 

    def __len__ (self):
        '''Return number of elements stored in the array.'''
        return self._n

    def __getitem__ (self, k):
        '''Return element at index k.'''
        if not -self._n <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k] 

    def append(self, obj):
        '''Add object to end of the array.'''
        if self._n == self._capacity: 
            self._resize(2*self._capacity) 
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c): 
        '''Resize internal array to capacity c.'''
        B = self._make_array(c) 
        for k in range(self._n): 
            B[k] = self._A[k]
        self._A=B 
        self._capacity = c

    def _make_array(self, c): 
        '''Return new array with capacity c.'''
        return (c*ctypes.py_object)()

###############Testing###############
newArray = DynamicArray()
newArray.append(21)
newArray._resize(1)
newArray.append(30)
print(newArray.__len__())


