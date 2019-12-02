from graph import *
"""«4»: Slide 66Квадрат не может выйти за границы синего квадрата, сразу останавливается при столкновении со стенкой. 
"""
dx = 5
dy = 3

def update():
    global dx , dy
    if xCoord(obj) > 370: #проверка что мы подошли к правой стенке квадрата
        dx = 0
        dy = 0
    elif xCoord(obj) < 20: #проверка что мы подошли к левой стенке квадрата
        dx = 0
        dy = 0
    moveObjectBy(obj, dx , dy )
#

def keyPressed(event):
  global dx, dy #глобальные переменные скорости по горизонтали и вертикали
  if event.keycode == VK_LEFT:
      dx = -5
      dy = 0
  elif event.keycode == VK_RIGHT:
      dx = 5
      dy = 0

  elif event.keycode == VK_DOWN:
        dx = 0
        dy = 5
  elif event.keycode == VK_UP:
        dx = 0
        dy = -5
  elif event.keycode == VK_SPACE:
       close()
onKey(keyPressed)

brushColor("blue")
rectangle(0, 0, 400, 400)
x = 100
y = 100
z = 10
penColor("yellow")
brushColor("yellow")
obj = rectangle(x, y, x+20, y+20)
onTimer(update, 50)

run()
