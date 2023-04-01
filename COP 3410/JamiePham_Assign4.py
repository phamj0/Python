'''
Name: Jamie Pham
Date: March 29th 2023
Assignment #: 4

This assignment goes over Chapter 4 questions.

'''

# 1
def palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])


print(palindrome('racecar'))
print(palindrome('gohangasalamiimalasagnahog'))
print(palindrome('yes'))


# 2
class Matrix:

    def __init__(self, m1, m2):
        '''Creating instance of the Matrices'''
        self.m1 = m1
        self.m2 = m2

    def get_m1(self):
        '''Returns first Matrice'''
        return self.m1
    
    def get_m2(self):
        '''Returns second Matrice'''
        return self.m2
    
    def set_m1(self, m1):
        '''Sets m1 to a new Matrix'''
        self.m1 = m1

    def set_m2(self, m2):
        '''Sets m2 to a new Matrix'''
        self.m2 = m2

    def addition(self):
        '''Adds both matrices'''
        if len(self.m1[0]) != len(self.m2[0]):      # raises IndexError 
            raise IndexError('Matrix dimensions must be equal')
        additionMatrix = []
        for row in range(len(self.m1)):
            newRow = []                             # creates new list object to store result into a row
            for col in range(len(self.m1[0])):
                newRow.append(self.m1[row][col] + self.m2[row][col])
            additionMatrix.append(newRow)           # adds new row made to mimic a matrix
        return additionMatrix
                
        
    def multiplication(self):
        '''Multiplies both matrices'''
        if len(self.m1[0]) != len(self.m2[0]):
            raise IndexError('Matrix dimensions must be equal')
        multiplyMatrix = []
        for row in range(len(self.m1)):
            newRow = []
            for col in range(len(self.m2[0])):
                 newRow.append(self.m1[row][col] * self.m2[row][col])
            multiplyMatrix.append(newRow)
        return multiplyMatrix


############################### Testing the class ######################################## 
if __name__ == "__main__":
 matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

 matrix2 = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]

 matrix3 = [[3, 2, 1], 
             [6, 5, 4], 
             [9, 8, 7]]

 matrix4 = [[3, 2, 1], 
             [6, 5, 4], 
             [9, 8, 7]]

 newMatrix = Matrix(matrix1, matrix2)

 print(newMatrix.get_m1())
 print(newMatrix.get_m2())
 print(newMatrix.addition())
 print(newMatrix.multiplication())

 newMatrix.set_m1(matrix3)
 newMatrix.set_m2(matrix4)
 print(newMatrix.get_m1())
 print(newMatrix.get_m2())
 print(newMatrix.addition())
 print(newMatrix.multiplication())

