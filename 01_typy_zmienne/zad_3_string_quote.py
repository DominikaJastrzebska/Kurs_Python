"""
3. Do zmiennej quote przypisz zdanie:
„Honesty is the first chapter in the book of wisdom.”, a następnie:
Policz wszystkie znaki w napisie
Nie modyfikując zmiennej wyświetl słowo wisdom
Wyświetl tylko pierwszą połowę tekstu
Wyświetl tylko kropkę
Wyświetl od połowy tylko co trzecią literę cytatu
Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
Wyświetl cały cytat odwrotnie
Zamień wisdom na słowo friendship
"""


quote = "Honesty is the first chapter in the book of wisdom."

print('Liczba znakow w napisie:', len(quote))
print('Wyswietlone slowo wisdom:', quote[-7:-1])
print('Wyswietlone slowo wisdom:', quote[44:50])
print('Wyswietlona pierwsza polowa tekstu:', quote[0:len(quote)//2])
print('Wyswietlona kropka:', quote[-1])
print('Wyswietlona kropka:', quote[50])
print('Wyswietlona od polowy co trzecia litera z cytatu:', quote[len(quote)//2::3])
print('Wyswietla napis: ‘Hnsyi h is hpe ntebo fwso.’:', quote[0:51:2])
print('Wyswietla napis: ‘Hnsyi h is hpe ntebo fwso.’:', quote[::2])
print('Wyswietla caly cytat odwrotnie:', quote[::-1])
# print('Wyswietla caly cytat odwrotnie:', quote[-51:-1])

print('Zamienia slowo wisdom na friendship:', quote.replace('wisdom', 'friendship'))