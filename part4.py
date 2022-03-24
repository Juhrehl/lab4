import turtle

t = turtle.Turtle()

def position_turtle(x, y):
  t.hideturtle()
  t.penup()
  t.goto(x,y)
  t.showturtle()
  t.pendown()
  
def stairs_down(x, steps):
  for i in range (steps):
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.left(90)

position_turtle(-100,100)
stairs_down(50, 1)
position_turtle(-100,90)


turtle.getscreen()._root.mainloop()