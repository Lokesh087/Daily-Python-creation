import turtle

screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#071525")
screen.title("Aurora Waves")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.hideturtle()

colors = ["#55e6c1", "#48dbfb", "#a29bfe", "#fd79a8", "#feca57"]

for band in range(5):
    pen.penup()
    pen.goto(-260, 100 - band * 48)
    pen.setheading(0)
    pen.pendown()
    pen.pencolor(colors[band])
    for step in range(52):
        pen.forward(10)
        pen.left(5 if (step + band) % 2 == 0 else -5)

for x in range(-220, 261, 55):
    pen.penup()
    pen.goto(x, 190 + (x % 3) * 7)
    pen.dot(4, "#ffffff")

turtle.done()
