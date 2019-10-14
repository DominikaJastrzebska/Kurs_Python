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
