'''
3▹ Wyświetl tylko 5 pierwszych linii
'''

import random

quotes = 'cytaty.txt'

with open(quotes, 'r') as f:
    lines_quotes = f.readlines()

for line in lines_quotes[0:5]:
    print(line.strip())
