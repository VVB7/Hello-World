from graph import *
"""Квадрат двигается при нажатии стрелок, однако не может выйти за границы синего квадрата: 
"""

brushColor("blue")
rectangle(0, 0, 400, 400)
x = 100
y = 100
z = 10
penColor("yellow")
brushColor("yellow")
obj = rectangle(x, y, x+20, y+20)


def keyPressed(event):
    if event.keycode == VK_LEFT and xCoord(obj) > 0:
        moveObjectBy(obj, -5, 0)
    elif event.keycode == VK_RIGHT and xCoord(obj) < 370:
        moveObjectBy(obj, 5, 0)
    elif event.keycode == VK_DOWN and yCoord(obj) < 370:
        moveObjectBy(obj, 0, 5)
    elif event.keycode == VK_UP and yCoord(obj) > 40:
        moveObjectBy(obj, 0, -5)

onKey(keyPressed)

run()
