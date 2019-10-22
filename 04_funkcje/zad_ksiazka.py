'''
1. Napisz funkcje, ktora pyta uzytkownika o pary ksiazka + ocena i zapisuje je w programie
2. Napisz funkcje, ktora zapyta o ocene ksiazki i wyswietli ksiazke wraz z ta ocena, jesli
ksiazka o takiej ocenie istnieje
3. W prosty sposob obsluz blad uzytkownika - uzytkownik zapyta o numer, ktory nie istnieje
'''

# def para(book, grade):
#     dict = {book:grade}
#     print(dict)
#     return dict
#
#
# dict1 = {input('Podaj tytul ksiazki: '):input('Podaj ocene ksiazki: ')}
#
# para(dict1)

# print('------------------------')
# books = {}
# counter = int(input(('Ile ksiazek chcesz dodac? ')))
# for _ in range(counter):
#     title = input('Podaj tytul ksiazki: ')
#     grade = input('Podaj ocene: ')
#     books[title] = grade
# print(books)


# def add_book(dict_books):
#     counter = int(input(('Ile ksiazek chcesz dodac? ')))
#     for _ in range(counter):
#         title = input('Podaj tytul ksiazki: ')
#         grade = input('Podaj ocene: ')
#         dict_books[title] = grade
#     return dict_books
#
# books = {}
# library = add_book(books)
# print(library)

print('------------------------------')

def add_book():
    dict_books = {}
    counter = int(input(('Ile ksiazek chcesz dodac? ')))
    for _ in range(counter):
        title = input('Podaj tytul ksiazki: ')
        grade = input('Podaj ocene: ')
        dict_books[title] = grade
    return dict_books

# g = input('Podaj ocene ksiazki, jaka chcesz przeczytac: ')
# if g in books.values():
#     for title, grade in books.items():
#         if grade == g:
#             print(title, ' - ocena: ', grade)
# else:
#     print('Nie ma ksiazki o takiej ocenie')


def read_book_by_grade(libr):
    g = input('Podaj ocene ksiazki, jaka chcesz przeczytac: ')
    if g in libr.values():
        for title, grade in libr.items():
            if grade == g:
                print(title, ' - ocena: ', grade)
    else:
        print('Nie ma ksiazki o takiej ocenie')

books = add_book() #przypisujemy do zmiennej, bo kod cos zwraca
print(books)
read_book_by_grade(books)


print('*'*10)



