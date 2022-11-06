import turtle


def alex_square(a, b):
    """Make a square"""
    for y in ['pink', 'blue', 'yellow', 'white']:
        a.color(y)
        a.forward(b)
        a.right(90)


wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Homework 2')

alex = turtle.Turtle()
alex.pensize(15)

size = 50
for x in range(5):
    alex_square(alex, size)
    size = size + 5
    alex.forward(10)
    alex.right(18)

wn.mainloop()
