class Vertebrate:  # kregowce
    backbone = True

    def __init__(self):
        print('Szkielet wewnętrzny kręgowców zbudowany jest z tkanki łącznej chrzęstnej, kostnej lub obu tych tkanek.'
              '\nRandom kregowiec')

    def desc(self):
        print('Zewnętrzną pokrywę ciała kręgowców stanowi skóra')

    # def __str__(self):  #wskazuje, co ma sie wyswietlic na samo print obiekt, mozna zakomentowac i sprawdzic
    # co wyswietla
    #     return "I'm vertebrate"


# v1 = Vertebrate()
# print(v1)


class Cat(Vertebrate):  #dziedziczenie, to czego nie ma dostaje od rodzica, dopoki nie nadpiszemy
    def __init__(self, name):  #nadpisujemy inicjalizacje i wykonalo sie to init, a nie z rodzica
        print("I'm cat")
        self.name = name

    def desc(self):
        super().desc()  #ometoda specjalna, odwolanie do klasy nadrzednej - rodzica
        print('Koty sa super')
        super().__init__()

    def sound(self):
        return 'miau'


ver = Vertebrate()
kitty = Cat('Kitty')
# print(kitty)
print(kitty.name)
print(kitty.backbone)
kitty.desc()
