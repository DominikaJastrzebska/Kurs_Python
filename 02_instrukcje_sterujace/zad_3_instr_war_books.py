'''
3. Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce. W
zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry,
ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.
'''

opinia_1 = float(input('Podaj opinie, co myslisz o fabule ksiazki/ocena 1-10: '))
opinia_2 = float(input('Podaj opinie, co myslisz o bohaterach ksiazki/ocena 1-10: '))
opinia_3 = float(input('Podaj opinie, co myslisz o ksiazce/ocena 1-10: '))
srednia = (opinia_1 + opinia_2 + opinia_3)/3

if srednia > 7:
    ocena = 'bardzo dobry'
elif 5 <= srednia <= 7:
    ocena = 'przecietna'
else:
    ocena = 'nie warta uwagi'
print('Twoja opinia o ksiazce to ', ocena)
