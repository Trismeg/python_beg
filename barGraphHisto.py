from graphics import *
import random

#create array of sums of 10 random numbers (0 to 1)
b=[]
for i in range(1000):
    s=0
    for j in range(10):
        s=s+random.uniform(0,1)
    b=b+[s]

#create histogram array
h=[]
for i in range(10):
    h=h+[0]

#fill in histogram array
for i in range(1000):
    g=int(b[i])
    h[g]=h[g]+1

#Length of array
L=len(h)
#Max value of number
M=500

#a=[]
#for i in range(10):
#    a=a+[random.uniform(0,M)]

win=GraphWin()
win.setCoords(-0.2,0,L,M+0.2)

#Array of bottom left points
bl=[]
for i in range(L):
    bl=bl+[Point(i,0)]

#Array of top right points
tr=[]
for i in range(L):
    tr=tr+[Point(i+1,h[i])]

#Array of Rectangles
rec=[]
for i in range(L):
    rec=rec+[Rectangle(bl[i],tr[i])]

for i in range(L):
    rec[i].draw(win)

