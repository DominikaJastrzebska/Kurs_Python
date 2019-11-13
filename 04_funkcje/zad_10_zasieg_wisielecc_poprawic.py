'''
10▹ Stwórz grę wisielec “bez wisielca”.
Komputer losuje wyraz z dostępnej w programie listy wyrazów.
Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
Użykownik podaje literę.
Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
“Trafione!” oraz napis ze znanymi literami.
W przeciwnym wpadku pokaż komunikat:
“Nie trafione, spróbuj jeszcze raz!”.
Możesz ograniczyć liczbę prób do np. 10.
'''

import random

words = ['company', 'country', 'day', 'eye', 'fact', 'family', 'government',
         'group', 'hand', 'home', 'month', 'mother']


def menu():
    print('Welcome to hangman game')


def hangman():
    comp_choice = random.choice(words)
    print(comp_choice)
    underscore = []
    for letter in comp_choice:
        underscore.append('_')

    try_to_guess = False

    while not try_to_guess:
        print('Slowo do odgadniecia to: ', ' '.join(underscore))
        user_letter = input('Podaj litere, ktora wystepuje w slowie, aby przerwac gre wpisz exit ')
        if user_letter.lower() == 'exit':
            print('Przegrales, slowo do odgadniecia to: ', comp_choice)
            try_to_guess = True
        elif user_letter.lower() == comp_choice:
            print('Wygrales, zgadles slowo')
            break
        else:
            for position, letter in enumerate(comp_choice):
                if letter == user_letter:
                    underscore[position] = letter
            if ''.join(underscore) == comp_choice:
                print('Wygrales!')
                try_to_guess = True
    play_again()


def play_again():
    answer = input('Chcesz zagrac jeszcze raz? y/n ')
    if answer.lower() == 'y':
        hangman()
    else:
        exit()


hangman()

