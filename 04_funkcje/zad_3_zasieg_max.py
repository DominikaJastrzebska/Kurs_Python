'''
3▹ Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb.
maximum_of(a, b, c).
'''

def max_func(a, b, c):
    if a <= b:
        if c <= a:
            print('Max: ', b) #cab
        else:
            if b <= c:
                print('Max: ', c) #abc
            else:
                print('Max:', b) #acb
    else:
        if c <= b:
            print('Max: ', a) #cba
        else:
            if c <= a:
                print('Max: ', a), #bca
            else:
                print('Max: ', c) #bac


a = float(input('Podaj liczbe a: '))
b = float(input('Podaj liczbe b: '))
c = float(input('Podaj liczbe c: '))

max_func(a, b, c)