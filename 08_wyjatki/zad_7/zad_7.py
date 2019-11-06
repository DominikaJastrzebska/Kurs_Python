'''
7▹ Wróć do pierwszego zadania z lekcji o plikach, zmodyfikuj go tak, aby to użytkownik podawał nazwę pliku
z cytatami. Pamiętaj, by użytkownik po wykonaniu błędnej akcji (np. literówki w nazwie pliku)
miał możliwość poprawić swój błąd.
'''

import random

while True:
    try:
        quotes = input('Your file: ')
        with open(quotes, 'r') as fopen:
            lines_quotes = fopen.readlines()
        print(lines_quotes)
        break
    except FileNotFoundError as e:
        print(e)
        lines_quotes = ['bledna nazwa pliku - ', 'bledna nazwa pliku - ']

quote_of_day = random.choice(lines_quotes).strip()
quote_of_day = quote_of_day.split('-')
print(quote_of_day)

print('Quote of the day is:')
print(''.center(100, '*'))
print(quote_of_day[0].center(100))
print(('~'+quote_of_day[1]).center(100))
print(''.center(100, '*'))