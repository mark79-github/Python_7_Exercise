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

side = 40

kanatica(-100, -100, side, 'violet', 'pink')
kanatica(0, -100, side, 'blue', 'navy')
kanatica(100, -100, side, 'green', 'lightgreen')

kanatica(-100, 80, side, 'navy', 'pink')
kanatica(0, 80, side, 'orange', 'yellow')
kanatica(100, 80, side, 'red', 'orange')

p.done()