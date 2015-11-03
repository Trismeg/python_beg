

def baby():
    print "wa"


def multi_baby(n):
    for i in range(n):
        baby()

def multi_print(string,n):
    for i in range(n):
        print string
    

def isPrime(n):
    state=True
    for i in range(2,n):
        if n%i==0:
            state=False
    return state
        
        

#multi_baby(7)

#multi_print("hello",5)

def tellMe(x):
    if isPrime(x):
        print str(x)+" is a prime number"
    else:
        print str(x) + " is a composite"


#tellMe(10)
#tellMe(11)



