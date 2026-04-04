import turtle
sc = turtle.Screen()
don = turtle.Turtle()
# дефинираме изчертаването на един триъгълник
def triangle(side,color1):
  don.color(color1)
  don.begin_fill()
  don.pendown()
  for count in range(3):
    don.forward(side)
    don.left(120)
  don.end_fill()
  don.penup()
# дефиниране на мотива
def kanatica(x,y,side,color1,color2):
  don.goto(x,y)
  don.pendown()
  don.color(color1)
  for br in range(3):
    don.right(120)
    triangle(side,color1)
  don.color(color2)
  don.left(60)
  don.begin_fill()
  for i in range(2):
    don.forward(side)
    don.left(60)
    don.forward(side)
    don.left(120)
  don.end_fill()
  don.goto(x,y+side*1.7)
  don.color(color1)
  for br in range(3):
    don.right(120)
    triangle(side,color1)
  don.left(300)
  don.penup()
# изчертаване на декоративни композиции с този мотив
don.penup()
color1 = 'red'
color2 = 'orange'
side = 40
kanatica(0,0,side,color1,color2)