'''
2▹ Utwórz dowolną krotkę zawierającą kilka wartości np. 10. Pozwól użytkownikowi podać dowolny index
oraz wartość. Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd
'''

my_tuple = (1, 2, 3, 'lalala', 'o', [8, 9, 'a'], 8, {1:'a', 2:'b', 3:'c'}, {'a', 'b', 'c', 'd'} )

index = input('Podaj dowolny indeks: ')
value = input('Podaj dowolna wartosc: ')

try:
    my_tuple[index] = value
except TypeError as e:
    print(e)

print(my_tuple)