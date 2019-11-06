'''
3▹ Stwórz listę 10 elementową (różne typy!). Pozwól użytkownikowi podać dowolny index. Podziel 1 przez
liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.
'''

my_list = [1, 2, 3, 'a', 'b', 'c', True, False, [1, 2], {1, 2}, (1, 2)]
index = int(input('Podaj dowolny indeks: '))
try:
    result = 1/my_list[index]
except TypeError as e:
    print(e)
    result = 'nie zdefiniowano'

print(result)