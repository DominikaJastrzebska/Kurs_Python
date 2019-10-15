zmienna = input('Podaj dowolna zmienna: ')
if len(zmienna) > 5:
    print('Zmienna jest dluzsza od 5.')
else:
    print('Zmienna jest krótsza niz 5.')
if 'a' in zmienna:
    zmienna = zmienna.replace('a', 'z')
else:
    print('Zmienna nie zawiera litery a.')
print(zmienna)