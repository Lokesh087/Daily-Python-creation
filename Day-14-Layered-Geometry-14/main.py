import turtle
screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#111827")
screen.title("Layered Geometry 14")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
sides = 5
for layer in range(12):
    pen.pencolor(["#7bdff2", "#cdb4db", "#ff5c8a"][layer % 3])
    for _ in range(sides):
        pen.forward(89 + layer * 3)
        pen.left(360 / sides)
    pen.left(27)
pen.hideturtle()
turtle.done()
