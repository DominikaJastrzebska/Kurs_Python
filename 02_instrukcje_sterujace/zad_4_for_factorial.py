'''
4. Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez
użytkownika, ale nie większe niż 8).
'''

N = int(input('Podaj liczbe naturalna w przedziale 0 - 8: '))

factorial = 1

if N >= 9 or N <0:
    print('Nieprawidlowa liczba, podaj liczbe naturalna od 0-8: ')
else:
    for i in range(0, N+1):
        if i > 0:
            factorial = factorial * i
            print(str(i)+'! =', factorial)
        else:
            print(str(i)+'! =', 1)
