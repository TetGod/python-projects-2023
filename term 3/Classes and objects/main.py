import Landon
import person

Landon = person.Person("Eric",True,True,False,"Blue","Male",68,130,42.,"o-","brown","God")
kaine = person.Person("Kaine",True,False,False,"brown","M",72,145,16,"o+","Rainbow","yes")
LandonN = person.Person("LandonN")
LandonN.speak("Hi My name is "+LandonN.name)
Landon.die()
print(Landon.isAlive)
print(Landon)
print(kaine)
print(LandonN)
print(person.Person.people_count)