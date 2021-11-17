class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print('So far: ',self.x)

a = PartyAnimal()
b = PartyAnimal()
print('For a: \n')
a.party()
a.party()
a.party()
a.party()
a.party()
print('\n\nFor b: \n')

b.party()
b.party()
b.party()
b.party()