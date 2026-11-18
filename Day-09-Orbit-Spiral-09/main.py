import turtle
screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#090b1a")
screen.title("Orbit Spiral 09")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
colors = ["#b2f7ef", "#f4a261", "#ffb347"]
for i in range(79):
    pen.pencolor(colors[i % len(colors)])
    pen.forward(i * 3)
    pen.right(87)
pen.hideturtle()
turtle.done()
