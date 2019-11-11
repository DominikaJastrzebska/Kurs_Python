'''
2▹ Napisać funkcję, która sprawdza czy liczba jest parzysta.
'''

print('Sposob 1'.center(30,'-'))

# def check_even_num(num):
#     if num % 2 == 0:
#         print(num, 'jest liczba parzysta.')
#     else:
#         print(num, 'jest liczba nieparzysta.')
#
#
# user_num = int(input('Podaj liczbe calkowita: '))
# check_even_num(user_num)

print('Sposob 2'.center(30,'-'))


def rest_from_division(num):
    return num % 2


def even_num(rest):
    if rest == 0:
        print(num, 'jest liczba parzysta.')
    else:
        print(num, 'jest liczba nieparzysta.')


num = int(input('Podaj liczbe calkowita: '))
rest = rest_from_division(num)
even_num(rest)


# print('Sposob 3'.center(30,'-'))
# def even_num_2():
#     user_num = input('Podaj liczbe calkowita: ')
#     if user_num % 2 == 0:
#         print(user_num, 'jest liczba parzysta')
#     else:
#         print(user_num, 'jest liczba nieparzysta'
#
#
# even = even_num_2()
