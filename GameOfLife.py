import random
from graphics import *

#this function creates an NxN array filled with zeros
def empty(N):
    a=[]
    for i in range(N):
        b=[]
        for j in range(N):
            b=b+[0]
        a=a+[b]
    return a

#this function fills the array a with a portion p of live cells
def fill(a,p):
    N=len(a)
    for i in range(N):
        for j in range(N):
            if random.uniform(0,1)<p:
                a[i][j]=1

def update(A,B):
    N=len(A)
    for i in range(N):
        for j in range(N):
            neigh=A[(i-1)%N,(j-1)%N]+A[(i-1)%N,(j)]+A[(i-1)%N,(j+1)%N]+A[(i),(j-1)%N]+A[(i),(j+1)%N]+A[(i+1)%N,(j-1)%N]+A[(i+1)%N,(j)]+A[(i+1)%N,(j+1)%N]
            if A[i][j]==0:
                if neigh==3:
                    B[i][j]=1
                else:
                    B[i][j]=0
            else:
                if neigh==2 or neigh==3:
                    B[i][j]=1
                else:
                    B[i][j]=0


def gen2Dgraphic(N):
    a=[]
    for i in range(N):
        b=[]
        for j in range(N):
            b=b+[Circle(Point(i,j),.49)]
        a=a+[b]
    return a


def drawArray(A,a,window):
#A is the array of 0,1 values representing the state of the game
#a is an array of Circle objects
#window is the GraphWin in which we will draw the circles
    N=len(A)
    for i in range(N):
        for j in range(N):
            if A[i][j]==1:
                a[i][j].draw(window)
            if A[i][j]==0:
                a[i][j].undraw()


    


#def 2Dgraphic(A):
#    N=len(A)
#    a=[]
#    for i in range(N):
#        b=[]
#        for j in range(N):
#            b=b+[Circle(Point(i,j),.49)]
#        a=a+[b]
    
#def graph2Darray(A,window):
#    N=len(A)
#    for i in range(N):
#        for j in range(N):
#            A[i][j].draw(window)


    
    
    
                
