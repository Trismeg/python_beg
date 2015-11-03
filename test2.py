from graphics import *

win=GraphWin()
win.setCoords(-10,-10,10,10)

for i in range(1,6):
    circ=Circle(Point(i,i),(2**0.5) * i)
    rec=Rectangle(Point(-i,-i),Point(0,0))
    t = Text(Point(-5,9-i), "yo")
    circ.draw(win)
    rec.draw(win)
    t.draw(win)
