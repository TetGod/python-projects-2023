class Person(object):
    people_count = 0
    languages = ["English","Spanish","French","Chinese","Japanese","Russian"]
    def __init__(self,name,alive=True,happy=False,mad=False,eyeColor="Hazel",gender="na",height=0,weight=0,age=0,bloodType="0",hairColor="Brown",race="na"):
        Person.people_count += 1
        self.name = name
        self.isAlive = alive
        self.happy = happy
        self.mad = mad
        self.language = ""
        self.eyeColor = eyeColor
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.bloodType = bloodType
        self.allergies = []
        self.hairColor = hairColor
        self.race = race

    def speak(self,speech):
        print(speech)
    def walk(self):
        print("walking")
    def run(self):
        print("running")
    def die(self):
        self.isAlive = False
        Person.people_count -=1
    def breath(self):
        pass
    def sleep(self):
        pass
    def jump(self):
        pass
    def grow(self,amount):
        self.height += amount
    def loseWeight(self,amount):
        self.weight -= amount

    def __str__(self):
        dis = self.name + "\n"
        dis += str(self.height) + "inches tall\n"
        dis += str(self.weight) + " pounds\n"
        dis += self.gender
        dis += self.eyeColor + " eyes\n"
        dis += self.hairColor + " hair\n"

        return dis




