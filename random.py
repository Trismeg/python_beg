import random

#print random.uniform(0.0,100.0)
a=[]

for i in range(20):
    a=a+[random.uniform(0.0,100.0)]

s=0.0
for i in range(len(a)):
    s=s+a[i]
avg=s/len(a)

s1=0.0
for i in range(len(a)):
    s1=s1+a[i]*a[i]
avgS=s1/len(a)


var=avgS-avg*avg
print var

s2=0.0
for i in range(len(a)):
    s2=s2+(a[i]-avg)*(a[i]-avg)

var2=s2/len(a)

print var2

stddev=var**(0.5)
print stddev


