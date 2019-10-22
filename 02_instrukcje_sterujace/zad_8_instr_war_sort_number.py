'''
8. Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. Znajdź
największą liczbę. Wyświetl liczby od największej do najmniejszej.
'''

number_1 = float(input('Podaj liczbe nr 1: ')) #1 1 2 3 1 3 2
number_2 = float(input('Podaj liczbe nr 2: ')) #2 3 1 1 3 2 3
number_3 = float(input('Podaj liczbe nr 3: ')) #3 2 3 2 2 1 1

if number_1 <= number_2 <= number_3:
    num_min = number_1
    num_mid = number_2
    num_max = number_3
elif number_1 <= number_3 <= number_2:
    num_min = number_1
    num_mid = number_3
    num_max = number_2
elif number_2 <= number_1 <= number_3:
    num_min = number_2
    num_mid = number_1
    num_max = number_3
elif number_3 <= number_1 <= number_2:
    num_min = number_3
    num_mid = number_1
    num_max = number_2
elif number_3 <= number_2 <= number_1:
    num_min = number_3
    num_mid = number_2
    num_max = number_1
elif number_2 <= number_3 <= number_1:
    num_min = number_2
    num_mid = number_3
    num_max = number_1

print(num_min, num_mid, num_max)