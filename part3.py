import turtle

t = turtle.Turtle()

def position_turtle(x, y):
  t.hideturtle()
  t.penup()
  t.goto(x,y)
  t.showturtle()
  t.pendown()
  
def stairs_down(x):
  for i in range (4):
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.left(90)

position_turtle(-100,100)
stairs_down(50)
position_turtle(-100,90)
stairs_down(50)

turtle.getscreen()._root.mainloop()