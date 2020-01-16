'''
2. Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100,
wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.
'''

number_1 = int(input('Podaj liczbe calkowita nr 1: '))
number_2 = int(input('Podaj liczbe calkowita nr 2: '))
sum_number = number_1 + number_2
if sum_number > 100:
    print(sum_number)
else:
    print ('Koniec')
