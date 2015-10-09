import time

start = time.time()


a=[]
num=2

while len(a)<1000:
    prime=True
    for x in range(len(a)):
        if num%a[x]==0:
            prime=False
    if prime:
        a=a+[num]
            
    num=num+1

print a


end = time.time()

print (end - start)
