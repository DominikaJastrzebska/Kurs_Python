'''
1▹ Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych
przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.
'''

names = input('Podaj imiona oddzielone przecinkiem: ')
list_of_names = names.split(',')
for name in list_of_names:
    print('Hello', name.title() + '!')
