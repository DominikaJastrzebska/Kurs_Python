'''
1▹ Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek. Każda z nich powinna dziedziczyć z nadrzędnej
klasy Ssaki. Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta. Utwórz obiekty klas - kot, pies i człowiek,
udowodnij, że rzeczywiście korzystają z klas rodziców.
'''


class Animal:
    def __init__(self):
        print('Zwierze')

    def desc(self):
        print(' za cechy odróżniające zwierzęta od innych organizmów przyjmuje się sposób odżywiania, '
              'brak ściany komórkowej, gromadzenie glikogenu oraz obecność (u wyżej uorganizowanych zwierząt) '
              'układu mięśniowego i nerwowego')


class Mammal(Animal):
    def __init__(self):
        print('Ssak')

    def desc(self):
        super().desc()
        print('zwierzęta należące do kręgowców, charakteryzujące się głównie występowaniem gruczołów mlekowych'
              ' u samic')


class Human(Mammal):
    def __init__(self, name):
        print('Czlowiek: ')
        self.name = name

    def desc(self):
        print('rodzaj ssaków naczelnych z rodziny człowiekowatych')
        super().desc()


class Dog(Mammal):
    def __init__(self, name):
        print('Pies: ')
        self.name = name

    def desc(self):
        print('udomowiona forma wilka szarego')


class Cat(Mammal):
    def __init__(self, name):
        print('Kot: ')
        self.name = name

    def desc(self):
        print('określenie każdego ssaka z rodziny kotowatych')
        super().desc()


# animal = Animal()
# ssaczek = Mammal()
# Mammal().desc()
# Ania = Human('Ania')
kotek = Cat('Mruczek')
kotek.desc()
Animal()
Animal().desc()
Mammal()
Mammal().desc()





