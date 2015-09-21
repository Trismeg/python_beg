a=4
b="prime"

for x in range(2,a/2+1):
    if a%x==0:
        b="composite"
        break
print "the number is "+b
    
