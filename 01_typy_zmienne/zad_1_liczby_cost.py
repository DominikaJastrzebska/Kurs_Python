'''
blicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.
'''

# dystans = 120
# spalanie = 6.4
# koszt_paliwa = 5.04
#
# koszt_wyprawy = dystans * spalanie / 100 * koszt_paliwa
# print(round(koszt_wyprawy,2))

distance = int(input('Podaj dystans: '))
l_per_100 = float(input('Podaj spalanie na 100 km: '))
price_per_l = float(input('Podaj cene paliwa za 1l: '))#skonczyc w domu i zrobic zadania
koszt_wyprawy = distance * l_per_100/100 * price_per_l
print('Koszt wyprawy wynosi', koszt_wyprawy, 'zł')