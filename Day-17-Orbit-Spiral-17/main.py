import turtle
screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#090b1a")
screen.title("Orbit Spiral 17")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
colors = ["#f4a261", "#ffb347", "#b2f7ef"]
for i in range(87):
    pen.pencolor(colors[i % len(colors)])
    pen.forward(i * 3)
    pen.right(95)
pen.hideturtle()
turtle.done()
