import turtle

jam = turtle.Turtle()
felipe = turtle.Turtle()

jam.color('pink')  # Change color
jam.pensize(15)  # Set pen width
felipe.color('blue')
felipe.pensize(15)

wn = turtle.Screen()
wn.bgcolor("black")  # Set the window background color
wn.title("Jam n Felipe!")  # Set the window title

felipe.left(45)
felipe.forward(70)
felipe.right(45)
felipe.forward(50)
felipe.right(45)
felipe.forward(60)
felipe.right(90)
felipe.forward(200)

jam.left(135)
jam.forward(70)
jam.left(45)
jam.forward(50)
jam.left(45)
jam.forward(60)
jam.left(90)
jam.forward(200)

wn.mainloop()
