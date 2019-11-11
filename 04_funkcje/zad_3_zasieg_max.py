'''
3▹ Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb.
maximum_of(a, b, c).
'''

# ('Sposob_1'.center(30, '-'))
# def max_func(a, b, c):
#     if a <= b:
#         if c <= a:
#             print('Max: ', b) #cab
#         else:
#             if b <= c:
#                 print('Max: ', c) #abc
#             else:
#                 print('Max:', b) #acb
#     else:
#         if c <= b:
#             print('Max: ', a) #cba
#         else:
#             if c <= a:
#                 print('Max: ', a), #bca
#             else:
#                 print('Max: ', c) #bac
#
#
# a = float(input('Podaj liczbe a: '))
# b = float(input('Podaj liczbe b: '))
# c = float(input('Podaj liczbe c: '))
#
# max_func(a, b, c)

# def maximum_of(a, b, c):
#     # a > b -> a > c -> a
#     # a > b -> b > c -> b
#     # a > b -> a > c -> c
#     if a > b:
#         maxab = a
#     else:
#         maxab = b
#     if maxab > c:
#         maxabc = maxab
#     else:
#         maxabc = c
#     return maxabc
# x = 3
# y = 8
# z = 2
#
# print(maximum_of(x, y, z))

# print('Sposob 3'.center(30, '-'))

# def maximum_of(a, b, c):
#     max_ab = a if a > b else b
#     max_abc = max_ab if max_ab > c else c
#     return max_abc
#
# x = 3
# y = 8
# z = 2
#
# print(maximum_of(x, y, z))

# print('Sposob 4'.center(30, '-'))


def max_of_2(first, second):
    # max_val = first if first > second else second
    return first if first > second else second


def maximum_of(a, b, c):
    # max_ab = max_of_2(a, b)
    # max_abc = max_of_2(max_of_2(a, b), c)
    return max_of_2(max_of_2(a, b), c)


def read_value():
    return int(input('Put integer value: '))


x = read_value()
y = read_value()
z = read_value()

result = maximum_of(x, y, z)
print('Max of: ', x, y, z, 'is', result)
