'''
4. Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5
znaków oraz czy zawiera literę a. Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały
napis.
'''

sentence = input('Podaj dowolna zmienna: ')
if len(sentence) > 5:
    print('Zmienna jest dluzsza od 5.')
else:
    print('Zmienna jest krótsza niz 5.')
if 'a' in sentence:
    sentence = sentence.replace('a', 'z')
else:
    print('Zmienna nie zawiera litery a.')

print(sentence)
