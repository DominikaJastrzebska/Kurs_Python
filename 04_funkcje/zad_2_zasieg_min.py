'''
2▹ Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).
'''

def min_func(a, b, c):
    if a <= b:
        if c <= a:
            print('Min: ', c) #cab
        else:
            print('Min: ', a) #acb acb
    else:
        if c <= b:
            print('Min: ', c) #cba
        else:
            print('Min: ', b), #bca bca

a = float(input('Podaj liczbe a: '))
b = float(input('Podaj liczbe b: '))
c = float(input('Podaj liczbe c: '))

min_func(a, b, c)