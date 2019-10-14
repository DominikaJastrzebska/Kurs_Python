imiona = input('Podaj imiona rozdzielone przecinkiem lub spacja: ')

imiona = imiona.split(' ')

for imie in imiona:
    print('Hello', imie)
