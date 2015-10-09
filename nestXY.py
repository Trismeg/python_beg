import random

xx=[]
for i in range(10):
    xx=xx+[range(10)]

r=[]
for i in range(10):
    r=r+[range(10)]

#print xx

yy=[]
for k in range(10):
    a=[]
    for j in range(10):
        a=a+[k]

    yy=yy+[a]

#print yy

z=range(10)
t=3.0


for j in range(10):
    for i in range(10):
        if random.uniform(0,10)<t:
            r[i][j]=1
        else:
            r[i][j]=0
 #   r=r+[z]
    #print z
print r

s=0
for j in range(10):
    for i in range(10):
        s=s+r[j][i]

rxx=[]
for i in range(10):
    rxx=rxx+[range(10)]

ryy=[]
for i in range(10):
    ryy=ryy+[range(10)]

for i in range(10):
    for j in range(10):
        rxx[j][i]=r[j][i]*xx[j][i]
        ryy[j][i]=r[j][i]*yy[j][i]

sxx=0
for i in range(10):
    for j in range(10):
        sxx=sxx+rxx[j][i]
