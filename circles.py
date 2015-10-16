from graphics import *
import random

wind=GraphWin()
wind.setCoords(0,0,10,10)

centers=[]
for i in range(10):
    centers=centers+[Point(random.uniform(0,10),random.uniform(0,10))]

circles=[]
for i in range(10):
    circles=circles+[Circle(centers[i],random.uniform(1,3))]

for i in range(10):
    circles[i].draw(wind)
