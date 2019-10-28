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
