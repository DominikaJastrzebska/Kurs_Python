'''
2▹ Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).
'''

# print('Sposob 1:')
# def min_func(a, b, c):
#     if a <= b:
#         if c <= a:
#             print('Min: ', c) #cab
#         else:
#             print('Min: ', a) #acb acb
#     else:
#         if c <= b:
#             print('Min: ', c) #cba
#         else:
#             print('Min: ', b), #bca bca
#
#
# a = float(input('Podaj liczbe a: '))
# b = float(input('Podaj liczbe b: '))
# c = float(input('Podaj liczbe c: '))
#
#
# min_func(a, b, c)


print('Sposob 2:')


def min_of_2(a, b):
    if a < b:
        return a
    else:
        return b


def minimum_of(a, b, c):
    return min_of_2(min_of_2(a, b), c)


def get_num():
    return int(input('Enter integer value: '))


a = get_num()
b = get_num()
c = get_num()
result = minimum_of(a, b, c)

print(f'Minimum of {a}, {b}, {c} is {result}')