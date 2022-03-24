import turtle

t = turtle.Turtle()

def position_turtle(x, y):
  t.hideturtle()
  t.penup()
  t.goto(x,y)
  t.showturtle()
  t.pendown()
  
def stairs_down(up, down, steps):
  for i in range (steps):
    t.fd(up)
    t.right(90)
    t.fd(down)
    t.left(90)

position_turtle(-100,100)
stairs_down(15,10, 5)
position_turtle(-100,90)
stairs_down(15,10, 5)

turtle.getscreen()._root.mainloop()