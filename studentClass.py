import os

class Student:

    numStu=0

    def __init__(self,n1,n2,nn,un):
        self.firstname=n1
        self.lastname=n2
        self.nickname=nn
        self.username=un
        Student.numStu=Student.numStu+1
        

    def getFullName(self):
        return self.firstname + "_" + self.lastname

    def getFirstName(self):
        return self.firstname

    def getLastName(self):
        return self.lastname

    def getNickName(self):
        return self.nickname

    def getUserName(self):
        return self.username

    def getNames(self):
        return [self.firstname,self.lastname,self.nickname,self.username]

    def intro(self):
        print "Hello my name is "+self.firstname

    def intro1(self):
        print "Hello my name is "+self.getFullName()

    def setFirstName(self,new):
        self.firstname=new

    def introTo(self,stu):
        print "Hello "+stu.getFirstName()+", my name is "+self.firstname

    def cloneRepo(self,repo):
        os.system("git clone https://github.com/"+self.username+"/"+repo+".git")

s1=Student("Barry","Bonds","Barbar","Trismeg")
s2=Student("Mike","Jackson","Jack","Thriller87")
#print s1.getNickName()
#print s1.getFullName()
#s1.intro1()
#s1.setFirstName("Larry")
#s1.intro1()
s2.introTo(s1)
#s1.cloneRepo("MassSpec")
print Student.numStu

