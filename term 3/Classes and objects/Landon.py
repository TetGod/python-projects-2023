import person

class Landon(person.Person):

    def __init__(self,alive,happy,mad,eyeColor,gender,height,weight,age,bloodType,hairColor,race):
        super(Landon, self).__init__()
        self.weight = 120
        self.language = person.Person.languages[0]
        self.happy = True
        self.mad = False
        self.bloodType = "o-"
        self.eyeColor = "hazel"
        self.height = "68"
        self.gander = "M"