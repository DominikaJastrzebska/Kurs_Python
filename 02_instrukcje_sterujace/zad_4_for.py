N = int(input('Podaj liczbe naturalna w przedziale 0 - 8: '))
silnia = 1
if N >= 9 or N <0:
    print('Nieprawidlowa liczba, podaj liczbe naturalna od 0-8: ')
else:
    for i in range(0, N+1):
        if i > 0:
            silnia = silnia * i
            print(str(i)+'! =', silnia)
        else:
            print(str(i)+'! =', 1)
