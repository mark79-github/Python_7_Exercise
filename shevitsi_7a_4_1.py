import turtle as p

def triangle(side, color):
   p.color(color)
   p.begin_fill()
   p.down()

   for count in range(3):
      p.forward(side)
      p.left(120)

   p.end_fill()
   p.up()

p.speed(3)
p.up()
p.goto(-50, -50)

triangle(100, "blue")

p.done()