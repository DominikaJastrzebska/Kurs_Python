'''
3▹ Stwórz własną implementację kolejki FIFO. Klasa kolejka (Queue) powinna na starcie przyjmować listę
elementów. Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki, sprawdzenie czy jest pusta,
dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).
Utwórz kilka obiektów klasy Queue z różnymi parametrami.
'''


class Fifo:
    def __init__(self, elements):
        self.elements = elements

    def show(self):
        print(self.elements)

    def __str__(self):   # ladnie wyswietlone, wyprintowane
        return ','.join(self.elements)

    def get(self):
        if len(self.elements) == 0:
            return 'Brak elementow'
        else:
            return self.elements.pop(0)

    # def put(self):
    #     value = input('Put element: ')
    #     self.elements.append(value)
    #     # return 'dodano'
    #     print(self.elements)

    def put(self, value):
        self.elements.append(value)


list_elem = ['a', 'b', 'c', 'd']
fifo1 = Fifo(list_elem) # tu przekazujemy liste elementow
print(fifo1.elements)
# print(fifo1)
# fifo1.show()
# print(fifo1.get())
# print(fifo1)
# print(fifo1.get())
# print(fifo1)
# print(fifo1.get())
# print(fifo1)
# print(fifo1.get())
# print(fifo1)
# print(fifo1.get())
# print(fifo1)
# fifo1.put()
print(list_elem)
# fifo1.put()
# print(fifo1)
# print(fifo1.put())
value = input('Podaj element: ')
fifo1.put(value)
print(fifo1)
