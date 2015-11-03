from graphics import *
import random

win=GraphWin()
win.setCoords(0,0,10,10)

centers=[]
for i in range(10):
    centers=centers+[Point(i,i)]

circles=[]
for i in range(10):
    circles=circles+[Circle(centers[i],0.49)]

for i in range(10):
    circles[i].draw(win)

for i in range(10):
    circles[i].undraw()
