#################
## EXAMPLE: simple Coordinate class
## Taken from MIT Courseware: MIT6_0001F16
#################
class Coordinate(object):
    """ A coordinate made up of an x and y value """
    def __init__(self, x , y ):
        """ Sets the x and y values """
        self.x = x
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_x(self,new_x = 0 ):
        self.x = new_x
    def set_y(self,new_y ):
        self.y = new_y
    def __str__(self):
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def distance(self, other):
        """ Returns the euclidean distance between two points """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5



c = Coordinate(3,4)
origin = Coordinate(0,0)
#print(c.x, origin.x)   #bad design against information hiding
print(c.distance(origin))
print(origin.distance(c))

print(c)  #this is possible due to __str__
c.set_x()
print(c)
c.set_y(-2)
print(c)
