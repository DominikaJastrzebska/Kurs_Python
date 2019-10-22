'''
1▹ Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych
przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.
'''

ciag_imion = input('Podaj imiona oddzielone przecinkiem: ')
lista_imion = ciag_imion.split(',')
for imie in lista_imion:
    print('Hello', imie.title() +'!')