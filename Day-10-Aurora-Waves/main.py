import turtle
import math

screen = turtle.Screen()
screen.setup(760, 680)
screen.bgcolor("#090b1f")
screen.title("Cosmic Lotus")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)

petal_colors = [
    "#ff5ca8", "#ff79c6", "#bd93f9",
    "#8be9fd", "#64dfdf", "#f1a7fe"
]

def draw_petal(radius, color):
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius, 60)
    pen.left(120)
    pen.circle(radius, 60)
    pen.left(120)
    pen.end_fill()

# Layered lotus petals
for layer in range(4):
    radius = 105 - layer * 17
    for i in range(12):
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(i * 30 + layer * 15)
        pen.forward(layer * 9)
        pen.pendown()
        draw_petal(radius, petal_colors[(i + layer) % len(petal_colors)])

# Glowing centre
pen.penup()
pen.goto(0, -12)
pen.dot(54, "#ffe08a")
pen.goto(0, -5)
pen.dot(28, "#fff4c2")

# Fine orbit rings
for radius, color in [(205, "#6c63ff"), (225, "#42d6c7"), (245, "#bd93f9")]:
    pen.penup()
    pen.goto(0, -radius)
    pen.setheading(0)
    pen.pendown()
    pen.pencolor(color)
    pen.pensize(2)
    pen.circle(radius)

# Small stars around the flower
stars = [
    (-285, 210), (-235, -185), (270, 190), (300, -120),
    (-315, 20), (185, 275), (80, -285), (-90, 285),
    (320, 55), (-170, 120), (145, -220), (-40, -300)
]
for i, (x, y) in enumerate(stars):
    pen.penup()
    pen.goto(x, y)
    pen.dot(5 + (i % 3) * 2, ["#ffffff", "#8be9fd", "#ffb8e8"][i % 3])

screen.update()
turtle.done()
