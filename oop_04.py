class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, name):
        self.name = name
        print('Constructed: ',self.name)

    def party(self):
        self.x = self.x + 1
        print('So far: ',self.x)

a = PartyAnimal('America')
b = PartyAnimal('China')

a.party()
b.party()
a.party()
