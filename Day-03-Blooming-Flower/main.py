import turtle
screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#101827")
screen.title("Blooming Flower")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
colors = ["#ff5c8a", "#ffb347", "#ffe66d", "#7bdff2", "#b2f7ef", "#cdb4db"]
for i in range(36):
    pen.color(colors[i % len(colors)])
    pen.circle(90, 60)
    pen.left(120)
    pen.circle(90, 60)
    pen.left(10)
pen.hideturtle()
turtle.done()
