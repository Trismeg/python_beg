from graphics import *
import math

wi=GraphWin()
wi.setCoords(-math.pi,-1.2,4.*math.pi,1.2)

p1=Point(-math.pi,0)
p2=Point(4.*math.pi,0)
p3=Point(0,-1.2)
p4=Point(0,1.2)

line1=Line(p1,p2)
line2=Line(p3,p4)

line1.draw(wi)
line2.draw(wi)


for i in range(-500,1000):
    wi.plot(i/999.*4.*math.pi,math.sin(i/999.*4.*math.pi))

