'''
3▹ Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.
'''

# print('Sposob 1'.center(30, '-'))
# def add_numbers_to_list():
#     num_list = []
#     counter = int(input('Ile liczb chcesz zsumowac? '))
#     for _ in range(counter):
#         num = int(input('Podaj liczbe: '))
#         num_list.append(num)
#     return num_list
#
# def add_numbers(num_list):
#     print(sum(num_list))
#
#
# numbers = add_numbers_to_list()
# add_numbers(numbers)

print('Sposob 2'.center(30, '-'))


def append_num_to_list():
    num_list = []
    while True:
        num = input('Podaj liczbe, nacisnij Q jesli chcesz przerwac ')
        if num == 'Q':
            break
        else:
            num_list.append(float(num))

    return num_list


def add_numbers_2(num_list):
    print(sum(num_list))


num_list = append_num_to_list()
add_numbers_2(num_list)