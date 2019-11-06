'''ciag fibonacciego'''


def string_fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return string_fibo(n-1) + string_fibo(n-2)


n = int(input('Podaj liczbe naturalna n, dla ktorej chcesz wyswietlic ciag Fibonacciego: '))

for number in range(n+1):
    print(number, string_fibo(number))
