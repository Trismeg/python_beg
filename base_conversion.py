ans =""
#this is static: c doesnt change
c=213
#this is dynamic: a will change
a=213
#this is base
b=2
#this is the exponent: e will change
e=0

while b**e<c:
    x=a%(b**(e+1))
    y=x/(b**(e))
    ans=str(y)+ans
    a=a-x
    e=e+1

print ans
