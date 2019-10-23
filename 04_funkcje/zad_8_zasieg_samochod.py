'''
8▹ Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako
zabytek.
Program zacznie ze stworzonym słownikiem o trzech kluczach:
marka (str)
model (str)
rocznik (int)
Wypisze ten słownik na ekran (bez żadnego formatowania)
Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
“Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
Jeśli nie spełnia powyższego warunku, wypisze komunikat:
“Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć,
czy progam również zmienia swoje zachowanie.
'''

my_car = {'marka': 'Fiat', 'model': '126p', 'rocznik': 1999}


def display_my_car():
    print(my_car)


def if_old():
    if 2019 - my_car['rocznik'] >= 25:
        print(f"Gratulacje! Twój samochód {my_car['marka']} może być zarejestrowany jako zabytek.")
    else:
        print(f"Twój samochód {my_car['marka']} jest jeszcze zbyt młody.")


display_my_car()
if_old()
