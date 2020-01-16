'''
1. Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika jest podzielna
przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.
'''

number = float(input('Podaj liczbe: '))
if number % 3 == 0:
    print(number, 'jest liczba podzielna przez 3.')
