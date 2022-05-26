import turtle

# Set pen's properties.
turtle.pensize(4)
turtle.pencolor('red')

# Change the turtle's direction.
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

# Maintain the window.
# Without mainloop(), the window will close after works done.
turtle.mainloop()