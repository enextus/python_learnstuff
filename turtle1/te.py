import turtle

d=turtle.Turtle()
l=25
d.penup()
n=7
for i in range(n):
 for j in range(n):
  d.dot()
  d.forward(l)
  d.backward(l*n)
  d.right(90)
  d.forward(l)
  d.left(90)

  d.left(90)
  d.forward(l)
  d.pendown()
  k=1

for j in range(3):
 d.forward(l*(n-k))
 d.right(90)

 for g in range(n-2):
  k=k+1
 
 for j in range(2):
  d.forward(l*(n-k))
  d.right(90)