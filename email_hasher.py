import hashlib

text="Hey man. How are you?"
recipient="mahoney@ef.com"
salt=0
state=True

num=5
lead=""
for i in range(num):
    lead=lead+"0"

while state:
    message=recipient+" "+text+" "+str(salt)
    hashe=hashlib.sha256(message).hexdigest()
    if hashe[0:num]==lead:
        state = False
    else:
        salt=salt+1

print "The proper salt is " + str(salt)
print message
print hashe
