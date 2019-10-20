'''
10.
Uzytkownik podaje dowolna liczbe N. Napisz, który wygeneruje slownik, wg zasady, ze kazdej liczbie
przyporzadkowany jest jej kwadrat (n : n * n).
Zalózmy, ze uzytkownik podal N = 8
Wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36
'''
N = int(input('Podaj dowolna liczbe naturalna N: '))
dict_square = {x:x**2 for x in range(N+1)}
print(dict_square)