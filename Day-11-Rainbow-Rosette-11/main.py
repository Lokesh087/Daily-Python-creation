import turtle
screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#171323")
screen.title("Rainbow Rosette 11")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
colors = ["#f4a261", "#ffb347", "#b2f7ef"]
for i in range(23):
    pen.pencolor(colors[i % 3])
    pen.circle(56, 120)
    pen.left(15)
pen.hideturtle()
turtle.done()
