#WE ARE LOOKING FOR THE POSITIVE ROOT OF THE FUNCTION f(x)=3-x*x
#this is the increment for derermining the slope of the function
dx=0.01
#this is the threshold
e=0.001
#this is the initial guess
x=1.0

while abs(3.0-x*x)>e:
    f=3.0-x*x
    f1=3.0-(x+dx)*(x+dx)
    s=(f1-f)/dx
    x=x+(-f)/s

print x
