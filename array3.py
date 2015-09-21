Q=[["Don","John",100,50,20],["Jack","Joe",20,90,100],["Sally","Sue",85,80,80]]
avg=0.
for i in range(3):
    avg=(Q[i][2]+Q[i][3]+Q[i][4])/3.
    print Q[i][0] + " has an average of " + str(avg)

    
