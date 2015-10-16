import time

start = time.time()


a=[]
num=2

while len(a)<100:
    prime=True
    for x in range(2,num/2+1):
        if num%x==0:
            prime=False
    if prime:
        a=a+[num]
            
    num=num+1

print a
            


end = time.time()

print (end - start)
