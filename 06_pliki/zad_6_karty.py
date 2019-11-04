'''
6▹ Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych. Sprawdź dla każdej kart jej
typ. Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt.
'''

# os.path.exist()

import os.path
from os import path


def visa(is_card, number_card):
    if not is_card:
        return False

    if len(number_card) == 13 or len(number_card) == 16:
        if number_card[0] == '4':
            #with open('visa.txt', 'a') as f:
                #f.write(f'\n{number_card}\n')
            return True


def mastercard(is_card, number_card):
    if not is_card:
        return False

    if len(number_card) == 16:
        # if int(number_card[0:2]) in range(51, 56) or int(number_card[0:4]) in range(2221, 2721):
        if int(number_card[0:2]) in range(51, 56) or int(number_card[0:4]) in range(2221, 2721):
            # with open('mastercard.txt', 'a') as f:
            #     f.write(f'\n{number_card}\n')
            return True


def americanexpress(is_card, number_card):
    if not is_card:
        return False

    if len(number_card) == 15:
        if int(number_card[0:2]) == 34 or int(number_card[0:2]) == 37:
            return True


filename = 'karty.txt'
with open(filename, 'r') as f:
    numbers = f.readlines()

cards = []
for number in numbers:
    cards.append(number.strip())

# number = input("podaj numer: ")
can_be_card_number = False

for number in cards:
    if len(number) > 16 or len(number) < 13:
        print('Wrong number', number)
    else:
        if number.isdecimal():
            print('Card', number)
            can_be_card_number = True
        else:
            print('Not a number', number)


for number in cards:
    if visa(can_be_card_number, number):
        print(number, 'visa')
        with open('visa.txt', 'a') as f:
            f.write(f'\n{number}')
    if mastercard(can_be_card_number, number):
        print(number, 'mastercard')
        with open('mastercard.txt', 'a') as f:
            f.write(f'\n{number}')
    if americanexpress(can_be_card_number, number):
        print(number, 'americanexpress')
        with open('americanexpress.txt', 'a') as f:
            f.write(f'\n{number}')
