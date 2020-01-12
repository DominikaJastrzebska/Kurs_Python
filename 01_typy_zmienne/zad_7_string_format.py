'''
7. Stwórz dwie dowolne zmienne przechowujące wartość liczbową i tekstową. Użyj funkcji format(), by
wyświetlić zdanie zawierające te wartości.
'''

name = input('Podaj swoje imie: ')
age = input('Podaj wiek: ')

print('Hello, my name is {name}, I am {age} years old'.format(name=name, age=age))
