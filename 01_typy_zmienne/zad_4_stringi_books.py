"""
4. Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
Połącz dane w jeden ciąg book za pomocą spacji
Policz liczbę wszystkich znaków w napisie book
"""

title = input('Podaj tytul ksiazki: ')
author = input('Podaj nazwisko autora: ')
number_of_pages = input('Podaj liczbe stron: ')

print('Czy tytul sklada sie z samych liter?', title.replace(' ', '').isalpha())
print('Czy liczba stron jest wartoscia liczbowa?', number_of_pages.isnumeric())
print('Czy autor sklada sie z samych liter?', author.replace(' ', '').isalpha())

print(title.title())
print(author.title()) #czy wszystkie wyrazy maja byc zamienione na duza litere?

book = (title, author, number_of_pages)
book = ' '.join(book)
print(book)

print('Liczba wszystkich znakow w ciagu book:', len(book))