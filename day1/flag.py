import turtle


# Set mode to be standard, which initial turtle heading to be right
# and set the positive angles to be counter clockwise.
turtle.mode("standard")


def draw_rectangle(x: float, y: float, width: float, height: float,
                   color="#FF0000", fill=True):
    """ draw a rectangle

    Args:
        x, y: Coordinate of the left-up point(starting point).
        width: Width of this rectangle.
        height: Height of this rectangle.
        color: The color of pen, default to be red.
        fill: Full fill or not, default to be true.
    """

    # Pull the pen up(no drawing when moving).
    turtle.penup()

    # Set turtle's position to starting point of this rectangle.
    turtle.setpos(x, y)
    # Pull the pen down(drawing when moving).
    turtle.pendown()

    turtle.pencolor(color)
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()

    # Go forward a length of width to the right.
    turtle.fd(width)
    # Turn right for 90 degrees.
    turtle.rt(90)

    turtle.fd(height)
    turtle.rt(90)

    turtle.fd(width)
    turtle.rt(90)

    turtle.fd(height)
    # Now the turtle back to staring point, and turn its heading back to origin.
    turtle.rt(90)
    turtle.penup()

    if turtle.filling():
        turtle.end_fill()


def draw_star(center_point: tuple, radius: float,
              towards_point=(0, 0), fill=True, color="#FFFF00"):
    """ draw a five angle star.

    Args:
        center_point: Coordinate of center point of the star.
        radius: Radius of the outer circle of the star.
        towards_point: Coordinate of one corner point towards to.
        fill: Full fill or not, default to be true.
        color: The color of pen, default to be yellow.
    """

    turtle.penup()

    x_center, y_center = center_point
    x_towards, y_towards = towards_point

    turtle.setpos(x_center, y_center)

    # Forward to the first point.
    turtle.left(turtle.towards(x_towards, y_towards) - turtle.heading())
    turtle.forward(radius)

    # Turn to the counter clockwise direction.
    turtle.left(90)

    # Get the positions of those five conner points.
    pos = []
    for i in range(0, 5):
        pos.append(turtle.pos())
        turtle.circle(radius, 72)

    # Turtle back to the first position finally.

    turtle.pendown()

    turtle.pencolor(color)
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()

    # 1 4 2 5 3
    turtle.goto(pos[3])
    turtle.goto(pos[1])
    turtle.goto(pos[4])
    turtle.goto(pos[2])
    turtle.goto(pos[0])

    if turtle.filling():
        turtle.end_fill()


def draw_flag(width):
    """ draw Chinese Flag

    The standard of the flag:
    http://www.chinaflag.org.cn/GuoQiZhishi/201474133055181.html

    Args:
        width: The width of the flag.

    """

    height = width * (2.0 / 3.0)
    half_width = width / 2.0
    half_height = height / 2.0

    draw_rectangle(-half_width, half_height, width, height)

    piece = half_width / 15
    # Calculate the location and size of those five stars.
    # The biggest one is No.1.
    center_1 = (-10 * piece, 5 * piece)
    radius_1 = 3 * piece
    draw_star(center_1, radius_1, (-10 * piece, 10 * piece))

    # Those four little stars from top to bottom.
    radius_little = piece
    towards_little = center_1

    x_list = [float(x * piece) for x in [-5, -3, -3, -5]]
    y_list = [float(x * piece) for x in [8, 6, 3, 1]]

    for center in zip(x_list, y_list):
        draw_star(center, radius_little, towards_little)

    turtle.hideturtle()


if __name__ == "__main__":
    # Range from 0 to 10.
    turtle.speed(0)

    draw_flag(1000)

    turtle.mainloop()
