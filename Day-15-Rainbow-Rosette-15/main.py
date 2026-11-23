import turtle
screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#171323")
screen.title("Rainbow Rosette 15")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
colors = ["#b2f7ef", "#f4a261", "#ffb347"]
for i in range(27):
    pen.pencolor(colors[i % 3])
    pen.circle(60, 120)
    pen.left(13)
pen.hideturtle()
turtle.done()
