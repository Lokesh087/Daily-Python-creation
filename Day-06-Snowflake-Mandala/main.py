import turtle

screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#071a2b")
screen.title("Snowflake Mandala")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.color("#8be9fd")

for _ in range(12):
    for length in (90, 35, 35):
        pen.forward(length)
        pen.backward(length)
        pen.left(45)
    pen.right(75)
    pen.forward(90)
    pen.backward(90)
    pen.left(30)

pen.hideturtle()
turtle.done()
