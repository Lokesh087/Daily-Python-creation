import turtle
screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#171323")
screen.title("Rainbow Rosette 19")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
colors = ["#ffb347", "#b2f7ef", "#f4a261"]
for i in range(31):
    pen.pencolor(colors[i % 3])
    pen.circle(64, 120)
    pen.left(11)
pen.hideturtle()
turtle.done()
