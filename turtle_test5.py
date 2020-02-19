import turtle
def drawSquare(t, sz):
  #"""Get turtle t to draw a square of sz side"""
  for i in range(4):
    t.forward(sz)
    t.left(90)
wn = turtle.Screen()
wn.bgcolor("lightblue")
alex = turtle.Turtle()
alex.color("orange")
for i in range(1,24):
  drawSquare(alex,100)
  alex.left(18)