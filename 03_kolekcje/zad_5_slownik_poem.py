'''
5▹ W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
"""Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""
Zadbaj o sposób wyświetlania np.:
szybko : 5
zbudź : 1
'''

'''
1. slownik = {} stworzenie pustego slownika
2. txt przechowuje tekst wierszyka
3. dzielimy tekst na pojedyncze wyrazy metoda split
dostaniemy liste
4. for
pobieramy elementy z listy i sprawdzamy, czy istnieje w slowniku
jesli jest to slownik[slowo] = +1
jesli nie istnieje to robimy nowy klucz
slownik[slowo] = 1
5. ladne wyswietlanie
szybko: 5
zbudz: 1
'''

dict = {}

poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

poem_list = poem.replace(',', '').split()

for word in poem_list:
    if word.lower() in dict:
        dict[word.lower()] += 1
    else:
        dict[word.lower()] = 1
print(dict)

for keys, values in dict.items():
    print(keys + ':', values)