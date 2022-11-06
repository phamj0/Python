import turtle

jam = turtle.Turtle()
jam.pensize(25)
jam.color('hot pink')

wn = turtle.Screen()
wn.bgcolor("black")  # Set the window background color
wn.title("Jam!")  # Set the window title

colors = ['hot pink', 'blue', 'yellow']
for x in colors:
    jam.color(x)
    jam.right(60)
    jam.forward(100)
    jam.right(60)

    jam.penup()


wn.mainloop()
