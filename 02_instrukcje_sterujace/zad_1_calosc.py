ciag_imion = input('Podaj imiona oddzielone przecinkiem: ')
lista_imion = ciag_imion.split(',')
for imie in lista_imion:
    print('Hello', imie.title() +'!')