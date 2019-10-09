#palindrom

czy_palindrom = 'Kobyła ma mały bok.'

czy_palindrom = czy_palindrom.replace(' ', '').replace('.', '').lower()
#print(czy_palindrom_1)
#print(czy_palindrom_1[::-1])
print(czy_palindrom == czy_palindrom[::-1])

