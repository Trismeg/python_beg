from graphics import *

wind=GraphWin()
wind.setCoords(0,0,10,11)

centers=[]
for i in range(10):
    centers=centers+[Point(5,1+i)]

circles=[]
for i in range(10):
    circles=circles+[Circle(centers[i],1)]

for i in range(10):
    circles[i].draw(wind)
