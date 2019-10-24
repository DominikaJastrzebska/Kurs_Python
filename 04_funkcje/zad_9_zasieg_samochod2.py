'''
9▹ Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75%
oryginalnych części. W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii
tak/nie.
Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
ponownie wyświetl zmieniony słownik
Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od
jego oryginalności. Dopisz odpowiednie komunikaty.
'''

# my_car = {'marka': 'Fiat', 'model': '126p', 'rocznik': 1999, 'czy_oryginalny': True}
#
#
# def display_my_car():
#     print(my_car)
#
#
# def if_old():
#     if 2019 - my_car['rocznik'] > 25:
#         print(f"Gratulacje! Twój samochód {my_car['marka']} może być zarejestrowany jako zabytek")
#     else:
#         print(f"Twój samochód {my_car['marka']} jest jeszcze zbyt młody.")
#
#
# def if_original():
#     if my_car['czy_oryginalny'] == True:
#         print('Ma oryginalne czesci')
#     else:
#         print('Nie ma org czesci')
#
#
# display_my_car()
# if_old()
# if_original()


my_car = {'marka': 'Fiat', 'model': '126p', 'rocznik': 1999, 'czy_oryginalny': True}

is_origin = False
age = 2019 - my_car['rocznik']

if age < 25:
    print('Samochod za mlody')
else:
    if my_car['czy_oryginalny'] is True:
        print('Samochod zabytkowy')
        is_origin = True
    else:
        print('Brak oryginalnych czesci')


def is_antique(is_original, is_old):
    if not is_original:
        return False
    if is_old >= 25:
        return True


is_antique(is_origin, age)