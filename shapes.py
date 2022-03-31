import turtle

t = turtle.Turtle()
t.speed(10)

def draw_square(color):
  t.color(color)
  t.begin_fill()
  
  for i in range (4):
    t.forward(20)
    t.right(90)
    
  t.end_fill()

def draw_row_odd(x, y):
  for i in range (4):
    x = x + 20
    position_turtle(x,y)
    draw_square("black")
    
    x = x + 20
    position_turtle(x, y)
    draw_square("white")
    
def draw_row_even(x, y):
  for i in range (4):
    x = x + 20
    position_turtle(x,y)
    draw_square("white")
    
    x = x + 20
    position_turtle(x, y)
    draw_square("black")
  
def position_turtle(x, y):
  t.hideturtle()
  t.penup()
  t.goto(x,y)
  t.showturtle()
  t.pendown()
  