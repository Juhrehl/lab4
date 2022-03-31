import turtle

t = turtle.Turtle()

def letter_J():
  t.pensize (5)
  t.right(90)
  t.circle(15, extent=180)
  t.forward(75)
  t.penup()
  t.right(90)

def letter_b():
  t.forward(75)
  t.pendown()
  t.pensize(5)
  t.left(90)
  t.back(100)
  t.right(90)
  
  for i in range(2):
    t.forward(50)
    t.left(90)

  t.forward(50)

letter_J()
letter_b()

turtle.getscreen()._root.mainloop()