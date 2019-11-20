import random


class Dog:

    def __init__(self, name, greed, color):
        self.name = name
        self.greed = greed
        self.color = color

    def bark(self):
        return 'Hau ' * random.randint(1, 10)

    def wag_tail(self):
        tail = ['~', '`', '^', '&']
        return random.choice(tail) * random.randrange(5, 20, 3)


obj_fela = Dog('Fela', 'labrador', 'white')
obj_scania = Dog('Scania', 'alaskan malamut', 'grey - white')

print(obj_fela.name)
print(obj_fela.wag_tail())
print(obj_fela.bark())