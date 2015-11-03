#create an NxN array
import random
import graphics


def grid(N):
    a=[]
    for i in range(N):
        b=[]
        for j in range(N):
            b=b+[0]
        a=a+[b]
    return a

def fill(a,thresh):
    N=len(a)
    for i in range(N):
        for j in range(N):
            k=random.uniform(0,100)
            if k>thresh:
                a[i][j]=1

def lookup(N):
    a=[]
    for i in range(N):
        b=[]
        for j in range(N):
            b=b+[[[(i-1)%N,(j-1)%N],[(i-1)%N,j%N],[(i-1)%N,(j+1)%N],[i%N,(j-1)%N],[i%N,(j+1)%N],[i+1,j-1],[i+1,j],[i+1,j+1]]]
        a=a+[b]
    return a



g=grid(5)
print g
fill(g,50)
print g
l=lookup(5)
print l


        
