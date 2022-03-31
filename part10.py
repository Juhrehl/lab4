import shapes as s

def draw_chess_board():
  x = -120
  y = 100
  for i in range (4):
    s.draw_row_even(x, y)
    y = y - 20
    s.draw_row_odd(x, y)
    y = y - 20

draw_chess_board()
  