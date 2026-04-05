import turtle

screen = turtle.Screen()
p = turtle.Turtle()
p.up()


def triangle(side):
    p.begin_fill()
    p.down()
    for count in range(3):
        p.forward(side)
        p.left(120)
    p.end_fill()
    p.up()


pos = 100
color = 'red'
side = 30
p.goto(pos, 0)
p.right(30)
p.color(color)

for br in range(3):
    triangle(side)
    pos = pos - side * 0.9
    p.goto(pos, 0)

pos = pos - side * 0.9
p.goto(pos, 0)
triangle(side * 2)
p.right(180)
triangle(side * 2)
pos = pos - 2 * 0.9 * side
p.goto(pos, 0)

for br in range(3):
    triangle(side)
    pos = pos - 0.9 * side
    p.goto(pos, 0)
