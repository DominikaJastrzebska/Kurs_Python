'''
1▹ Utwórz plik na pulpicie zawierający listę ok. 20 cytatów. Każdy cytat powinen się znaleźć w nowej linii.
Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:
Quote of the day is:
**************************************
be or not to be?
**************************************
zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami
plik z cytatami powinen również zawierać informację o autorze, wyświetl cytat i pod spodem autora
'''

import random

quotes = input('Your file: ')
with open(quotes, 'r') as fopen:
    lines_quotes = fopen.readlines()

quote_of_day = random.choice(lines_quotes).strip()
quote_of_day = quote_of_day.split('-')
print(quote_of_day)

print('Quote of the day is:')
print(''.center(100, '*'))
print(quote_of_day[0].center(100))
print(('~'+quote_of_day[1]).center(100))
print(''.center(100, '*'))
