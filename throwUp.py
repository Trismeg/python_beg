a=-9.8
v0=19.6
y0=10.0
dt=0.01
t=0.0

ymax=0.0

v=v0
y=y0

while y>0.0:
    t=t+dt
    v=v+a*dt
    y=y+v*dt
    if y > ymax:
        ymax=y

print "the time is "+str(t)+" sec"
print "the final velocity is "+str(v)+ " meter/sec"
print "the maximum height is "+str(ymax)+ " meter"

