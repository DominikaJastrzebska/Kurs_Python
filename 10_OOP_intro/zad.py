import random

dog = {
    'name': 'Pimpek',
    'breed': 'sznaucer',
    'age': 4,
    'color': 'white'
}


# class Dog: # to samo co class Dog()
#     pass
#
#
# obj_pimpek = Dog()
# obj_dyzio = Dog()
#
# # print(obj_pimpek)
# # print(obj_dyzio)
# #
# # a = 12
# # print(type(a))
# # print(type(obj_dyzio))
#
# obj_pimpek.name = 'Pimpek' # name - pole, atrybut
# obj_pimpek.breed = 'Jamnik'
# obj_pimpek.color = 'brown'
# print(obj_pimpek.name)
# print(obj_pimpek.color)

# teraz wypelniamy klase na podstawie powyzszego

# class Dog:
#     tail = True # ogon
#
#     def __init__(self, name, greed, age, color): # obiekt, instancja
#         self.name = name
#         self.greed = greed
#         self.age = age
#         self.color = color
#         self.pseudo = name + '-' + color
#
#
# obj_pimpek = Dog('Pimpek', 'Collie', 5, 'white')
# obj_dyzio = Dog('Dyzio', 'Cotton de tulear', 7, 'blond')
#
# print(obj_pimpek.name)
# print(obj_pimpek.color)
# print(obj_pimpek.pseudo)
# print(obj_dyzio.pseudo)
# print(obj_pimpek.tail)
# print(obj_dyzio.tail)
# print(Dog.tail)
# # print(Dog.name) tak nie mozna zrobic
#
# print(Dog.__dict__)
# print(obj_dyzio.__dict__)


class Dog: # klasa def strukture
    tail = True # ogon

    def __init__(self, name, greed, age, color): # obiekt, instancja, konstruktor, zapoczatkowanie istnienia obiektu, metoda specjalna
        self.name = name
        self.greed = greed
        self.age = age
        self.color = color

    def pseudo(self): #metoda
        adj = ['destroyer', 'powerfull', 'funny', 'sweet']
        return random.choice(adj) + '-' + self.name

    def bark(self):
        return 'hau' * self.age


obj_pimpek = Dog('Pimpek', 'Collie', 5, 'white') #przypisanie parametrow do obiektu
obj_dyzio = Dog('Dyzio', 'Cotton de tulear', 7, 'blond')

print(obj_pimpek.name)
print(obj_pimpek.pseudo())

print(obj_dyzio.pseudo())
print(Dog.pseudo(obj_dyzio)) # wywolujemy metode na obiekcie


names = 'Anna, Marta, Marek, Pawel'

print(names.split(','))
print(type(names))

print(str.split(names))  #print(str.split(names, ','))

print(obj_dyzio.bark())