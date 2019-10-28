import random


def random_quote(words):
    quote_of_day = random.choice(words).strip()
    return quote_of_day.split('-')


def show(quote_of_day):
    print('Quote of the day is:')
    print(''.center(100, '*'))
    print(quote_of_day[0].center(100))
    print(('~' + quote_of_day[1]).center(100))
    print(''.center(100, '*'))

filename = 'cytaty.txt'
with open(filename, 'r') as f:
    lines_quotes = f.readlines()

for i in range(3):
    sentence = random_quote(lines_quotes)
    print('---------')
    show(sentence)
