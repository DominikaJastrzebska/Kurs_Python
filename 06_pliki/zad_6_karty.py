'''
6▹ Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych. Sprawdź dla każdej kart jej
typ. Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt.
'''

# os.path.exist()

import os.path
from os import path

filename = 'karty.txt'
with open (filename, 'r') as f:
    numbers = f.readlines()

cards = []
for number in numbers:
    cards.append(number.strip())
print(cards)

can_be_card_number = False
for number in cards:
    if len(number) > 16 or len(number) < 13:
        print('Wrong number')
    else:
        if number.isdecimal():
            can_be_card_number = True
        else:
            print('Not a number')
