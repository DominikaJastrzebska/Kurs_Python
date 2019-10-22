'''
4▹ Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie. Powinna
zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.
'''

def number_in_range(a, b, x):
    if a <= x <= b:
        print('tak, liczba {} znajduje się w zadanym zakresie'.format(x))
    else:
        print('nie, liczba {} jest z poza zakresu'.format(x))


a = float(input(('Podaj poczatkowa liczbe zakresu: ')))
b = float(input('Podaj koncowa liczbe zakresu: '))
x = float(input('Podaj liczbe do sprawdzenia: '))

number_in_range(a, b, x)