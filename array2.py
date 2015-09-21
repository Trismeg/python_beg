a=["Billy","Bud",90,60,50]
b=["Anne","Chow",90,95,100]
c=["Jen","Bo",60,80,90]
m=[a,b,c]



for i in range(3):
    print "Dear " + m[i][0]+", you got a "+str(m[i][2])+", "+str(m[i][3])+", "+str(m[i][4])+" on three exams."
