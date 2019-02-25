class Pets:
    pet_list = []
    def __init__(self,pet_name,pet_age,pet_hungry):
        animal = []
        animal.append(pet_name)
        animal.append(pet_age)
        animal.append(pet_hungry)
        pet_list.append(animal)
    def is_hungry():
        for i in range(len(pet_list)):
            if pet_list[i][2] == True:
                whos_hungry(pet_list[i])
    def whos_hungry(pet):
        print(pet_list[0])

class Animal:
    def __init__(self,pet_name,pet_age):
        self.pet_name = pet_name
        self.pet_age = pet_age
        self.pet_hungry = True
    def eat(self):
        self.pet_hungry = False

class cat:
    species = 'Felis Cailus'
    kucing1 = Animal('bambang',10)
    def sound_kucing():
        print('Miaw')

class dog:
    species = 'Anjing'
    anjing1 = Animal('Budi',12)
    def sound_anjing():
        print('Guk')

class bird:
    species = 'burung'
    def sound_burung():
        print('cirp')
    
