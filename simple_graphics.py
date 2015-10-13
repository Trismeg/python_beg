from graphics import *

win=GraphWin()
win.setCoords(0,0,10,10)
t = Text(Point(5,5), "Centered Text")
t.draw(win)
p1=Point(1,1)
p2=Point(3,4)
r=Rectangle(p1,p2)
r.draw(win)
win.plot(8,9)
