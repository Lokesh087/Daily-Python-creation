import turtle
screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#090b1a")
screen.title("Neon Spiral")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
colors = ["#ff4d8d", "#a78bfa", "#38bdf8", "#34d399", "#facc15"]
for i in range(100):
    pen.pencolor(colors[i % len(colors)])
    pen.forward(i * 3)
    pen.right(91)
pen.hideturtle()
turtle.done()
