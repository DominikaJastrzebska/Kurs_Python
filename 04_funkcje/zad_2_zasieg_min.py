'''
2▹ Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).
'''

def min_func(a, b, c):
    if a <= b:
        if c <= a:
            print('Min: ', c) #cab
        else:
            if b <= c:
                print('Min: ', a) #abc
            else:
                print('Min:', a) #acb
    else:
        if c <= b:
            print('Min: ', c) #cba
        else:
            if c <= a:
                print('Min: ', b), #bca
            else:
                print('Min: ', b) #bca

a = float(input('Podaj liczbe a: '))
b = float(input('Podaj liczbe b: '))
c = float(input('Podaj liczbe c: '))