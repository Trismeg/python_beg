import random

#pick number of points
P=100000

#running sum
N=0.0

for i in range(P):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if (x*x+y*y)<1.:
        N=N+1.0

pi=4.0*N/P

print pi
    
