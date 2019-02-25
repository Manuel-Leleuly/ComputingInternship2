class Pets:
    pet_list = []
    def __init__(self):
        animal = []
        animal.append(self.pet_name)
        animal.append(self.pet_age)
        animal.append(self.pet_hungry)
        self.pet_list.append(animal)
    def is_hungry():
        for i in range(len(pet_list)):
            if pet_list[i][2] == True:
                whos_hungry(pet_list[i])
    def whos_hungry(pet):
        print(pet[0])

class Animal():
    def __init__(self,pet_name,pet_age):
        self.pet_name = pet_name
        self.pet_age = pet_age
        self.pet_hungry = True
        Pets.__init__(self)
    def eat(self):
        self.pet_hungry = False

class cat(Animal):
    species = 'Felis Catus'
    def __init__(self, pet_name, pet_age):
        Animal.__init__(self, pet_name, pet_age)
    def sound_kucing():
        print('Miaw')

class dog(Animal):
    species = 'Anjingus Gukgukus'
    def __init__(self, pet_name, pet_age):
        Animal.__init__(self, pet_name, pet_age)
    def sound_anjing():
        print('Guk')

class bird(Animal):
    species = 'Burungus Meong'
    def __init__(self, pet_name, pet_age):
        Animal.__init__(self, pet_name, pet_age)
    def sound_burung():
        print('cirp')
    
