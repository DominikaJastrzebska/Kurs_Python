#palindrom

'''
5. Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.:
Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy
wprowadzone wyrażenie jest palindromem.
'''
czy_palindrom = 'Kobyła ma mały bok.'

czy_palindrom = czy_palindrom.replace(' ', '').replace('.', '').lower()
#print(czy_palindrom_1)
#print(czy_palindrom_1[::-1])
print('Czy palindrom?', czy_palindrom == czy_palindrom[::-1])
