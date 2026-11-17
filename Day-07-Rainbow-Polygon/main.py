import turtle

screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#111827")
screen.title("Rainbow Polygon")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
colors = ["#ff595e", "#ffca3a", "#8ac926", "#1982c4", "#6a4c93"]

for layer in range(18):
    pen.pencolor(colors[layer % len(colors)])
    for _ in range(6):
        pen.forward(110 + layer * 4)
        pen.left(60)
    pen.left(20)

pen.hideturtle()
turtle.done()
