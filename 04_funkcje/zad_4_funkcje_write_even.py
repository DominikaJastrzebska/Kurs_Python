'''
4▹ Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów
 (wykorzystać funkcje z pkt 2)
'''

def append_num_to_list():
    num_list = []
    while True:
        num = input('Podaj liczbe, nacisnij Q jesli chcesz przerwac ')
        if num == 'Q':
            break
        else:
            num_list.append(int(num))
    return num_list


def rest_from_division(num_list):
    even_num_list = []
    odd_num_list = []
    for num in num_list:
        if num % 2 == 0:
            even_num_list.append(num)
        else:
            odd_num_list.append(num)
    return even_num_list

def show_even(num):
    print('Liczby parzyste: ')
    for numbers in num:
        print (numbers, end=', ') #JAK ZROBIC ZEBT PRINTOWALO Liczby parzyste: 2, 4, 6


nums = append_num_to_list()
print(nums)
rest = rest_from_division(nums)
show_even(rest)


