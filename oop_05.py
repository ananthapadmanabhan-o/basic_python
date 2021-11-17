class PartyAnimal:
    x = 0
    name = ''

    def __init__(self,name):
        self.name = name
        print('Constructed: ',self.name)

    def party(self):
        self.x = self.x + 1
        print('So far: ',self.x)

class CricketFan(PartyAnimal):
    points = 0
    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name,' points: ',self.points)

s = PartyAnimal('Jimmy')
s.party()

j = CricketFan('Arundhathi')
j.party()
j.six()

