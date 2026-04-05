import turtle as p


def triangle(side, color):
    p.color(color)
    p.begin_fill()
    p.down()
    for i in range(3):
        p.forward(side)
        p.left(120)
    p.end_fill()
    p.up()


def three_triangles(side, color1):
    for br in range(3):
        p.right(120)
        triangle(side, color1)


def paralelogram(side):
    p.begin_fill()
    for i in range(2):
        p.down()
        p.forward(side)
        p.left(60)
        p.forward(side)
        p.left(120)
        p.up()
    p.end_fill()


def kanatica(x, y, side, color1, color2):
    p.goto(x, y)
    p.color(color1)
    three_triangles(side, color1)

    p.color(color2)
    p.left(60)
    paralelogram(side)

    p.goto(x, y + side * 1.7)
    p.color(color1)
    three_triangles(side, color1)

    p.left(300)


p.speed(0)
p.up()

color1 = 'red'
color2 = 'green'
side = 30

x = -150
y = -175
for br in range(6):
    kanatica(x + br * side * 2, y, side, color1, color2)

x = -150
y = -72
for br in range(2):
    kanatica(x, y + br * side * 3.4, side, color1, color2)

x = -150
y = 130
for br in range(6):
    kanatica(x + br * side * 2, y, side, color1, color2)

x = 150
y = -72
for br in range(2):
    kanatica(x, y + br * side * 3.4, side, color1, color2)

p.done()
