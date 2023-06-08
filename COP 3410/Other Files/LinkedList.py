''''
Single Linked List Implementation
COP3410
Sareh Taebi
'''
class Node:
    '''Lightweight class for storing a singly linked node.'''

    def __init__(self, element, next):     # initialize node’s field
       self.element = element             # reference to user’s element
       self.next = next                   # reference to next node
  
    def getElement(self):                     # Accessor methods
        return  self.element
    
    def getNext(self):                       # Accessor methods
        return  self.next
    
    def setElement(self,new):                 # Modifier methods
        self.element  =  new
         
    def setNext(self,newNext): 
         self.next  =  newNext

    def __str__(self):
        return str(self.element)

        
if __name__ == "__main__":

# Node Creation
    x = Node(1,None)
    y = Node(2, None)

# Connect the nodes
    x.next = y
    y.next = None

    print(x.element, y.element)
