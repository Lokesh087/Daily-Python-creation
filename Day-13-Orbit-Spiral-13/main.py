import turtle
screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#090b1a")
screen.title("Orbit Spiral 13")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
colors = ["#ffb347", "#b2f7ef", "#f4a261"]
for i in range(83):
    pen.pencolor(colors[i % len(colors)])
    pen.forward(i * 3)
    pen.right(91)
pen.hideturtle()
turtle.done()
