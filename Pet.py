

class Pet:

    def __init__(self,petname,petspecies):
        self.name=petname
        self.species=petspecies

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def speak(self):
        if self.species=="Dog":
            print "Woof"
        else:
            if self.species=="Cat":
                print "Meow"
            else:
                print "Insert animal sound here"

    def intro(self,pet):
        print "Hello "+pet.getName()+" I am a " +self.species+" named "+self.name
        

p1=Pet("Bea","Dog")
p2=Pet("Tone","Cat")
#print p1.getName()+" is a "+p1.getSpecies()
#print p1
p1.intro(p2)
