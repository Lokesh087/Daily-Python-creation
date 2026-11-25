import turtle
screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#111827")
screen.title("Layered Geometry 18")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
sides = 3
for layer in range(16):
    pen.pencolor(["#ff5c8a", "#7bdff2", "#cdb4db"][layer % 3])
    for _ in range(sides):
        pen.forward(93 + layer * 3)
        pen.left(360 / sides)
    pen.left(31)
pen.hideturtle()
turtle.done()
