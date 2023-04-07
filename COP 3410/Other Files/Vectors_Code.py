## COP3410 : OOP, Operator Overloading
## Date: 09/14/2022

class Vector:
    '''Represent a vector in a multidimensional space.'''
    
    def __init__ (self, d):
        '''Create d-dimensional vector of zeros.'''
        self._coords = [0]*d
    
    def __len__ (self):
        '''Return the dimension of the vector.'''
        return len(self._coords)
    
    def __getitem__ (self, j):
        '''Return jth coordinate of vector.'''
        return self._coords[j]
    
    def __setitem__ (self, j, val):
        '''Set jth coordinate of vector to given value.'''
        self._coords[j] = val

    def __add__ (self, other):
        '''Return sum of two vectors.'''
        if len(self) != len(other): # relies on len method
            raise ValueError( 'dimensions must agree' )
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__ (self, other):
        '''Return True if vector has same coordinates as other.'''
        return self._coords == other._coords
    
    def __ne__(self, other):
        '''Return True if vector differs from other.'''
        return not self == other # rely on existing eq definition
    
    def __str__ (self):
        '''Produce string representation of vector.'''
        return '<' + str(self._coords) + '>' # adapt list representation

'''' more definitions for vectors '''''
    #def __neg__(self):
    #def __sub__(self,other):
    #def __mul__(self,other):
'''' implement on your own '''''

if __name__ == '__main__':
    v = Vector(5)                           # construct five-dimensional <0, 0, 0, 0, 0>
    for i in range(len(v)):                 
        v[i] = i                        #setitem function is helping us intialize values, setitem/getitem is used for sequences
    print(v)

    v[1] = 23                               # <0, 23, 0, 0, 0> (based on use of setitem )
    v[-1] = 45                              # <0, 23, 0, 0, 45> (also via setitem )
    print(v)
    print(v[4])                             # print 45 (via getitem )
    u = v + [5, 3, 10, -2, 1]               # <0, 46, 0, 0, 90> (via add )

    '''' how can you add both ways? '''''
    #v = [5, 3, 10, −2, 1] + u  It's illegal how can we make it happen?
    '''' implement on your own '''''

    print(u)                                # print <0, 46, 0, 0, 90>
    total = 0
    for entry in v:                         # implicit iteration via len and getitem
       total += entry
    str(u)
