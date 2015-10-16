from graphics import *
import random

#Length of array
L=10
#Max value of number
M=10
a=[]
for i in range(10):
    a=a+[random.uniform(0,M)]

win=GraphWin()
win.setCoords(-0.2,0,L,M+0.2)

#Array of bottom left points
bl=[]
for i in range(L):
    bl=bl+[Point(i,0)]

#Array of top right points
tr=[]
for i in range(L):
    tr=tr+[Point(i+1,a[i])]

#Array of Rectangles
rec=[]
for i in range(L):
    rec=rec+[Rectangle(bl[i],tr[i])]

for i in range(L):
    rec[i].draw(win)

