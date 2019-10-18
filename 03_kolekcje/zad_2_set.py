'''
2▹ Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2,
3, 4}. Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?
'''

text = '1234'
L_test = list(text)
print('Lista: ', L_test)
T_test = tuple(text)
print('Tupla czyli krotka: ', T_test)
S_test = set(text)
print('Set czyli zestaw: ', S_test)