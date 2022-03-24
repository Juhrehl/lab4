import turtle

t = turtle.Turtle()

def stairs_down(x):
  for i in range (4):
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.left(90)

stairs_down(50)

turtle.getscreen()._root.mainloop()