'''
Love Calculator
Stwórz grę inspirowaną miłosną wróżbą z czasów szkolnych. Zasady gry przedstawia to wideo.

Pobierz imiona zakochanych

Policz wystąpienia każdej z liter w obu imionach oraz słowie LOVE.

Redukuj liczbę elementów tablicy dodając pierwszą i ostatnią liczbę do siebie, tak długo, aż zostną dwie cyfry.

Dwie ostatnie cyfry tworzą wartość procentową dopasowania pary wg. wróżby.
'''


def get_names():
    """
    Function get two names
    return: list of two names
    """
    names = []
    name_woman = input('Enter woman\'s name: ')
    name_man = input('Enter man\'s name: ')
    names.append(name_woman)
    names.append(name_man)
    return names


def get_names_with_love(names):
    """
    param: list of two names
    return string
    """
    names_loves = names[0] + 'Loves' + names[1]
    return names_loves.lower()


def get_list_of_numbers(names_loves):
    """
    Function counts letters in word and return list of numbers
    param: string
    return list of numbers
    """
    numbers = []
    names_loves = names_loves.lower()
    for letter in names_loves:
        numbers.append(names_loves.count(letter))
        names_loves = names_loves.replace(letter, '')
        list_without_zero = list(filter(lambda x: x != 0, numbers))
    return list_without_zero


def add_numbers_from_list(list_without_zero):
    """
    Function takes the value - list of numbers and create new list of numbers by adding first and last number
    and remove it from previous list
    param: list of numbers
    return list of numbers
    """
    if len(list_without_zero) == 2:
        return list_without_zero
    else:
        next_number_list = []
        while len(list_without_zero) >= 1:
            if len(list_without_zero) >= 2:
                next_number_list.append(list_without_zero.pop(0) + list_without_zero.pop(-1))
            else:
                next_number_list.append(list_without_zero.pop())
        return add_numbers_from_list(next_number_list)
    # next_number_list = []
    # while len(list_without_zero) >= 1:
    #     if len(list_without_zero) >= 2:
    #         next_number_list.append(list_without_zero.pop(0) + list_without_zero.pop(-1))
    #     else:
    #         next_number_list.append(list_without_zero.pop())
    # return next_number_list


def show_answer(names, next_number_list):
    """
    param: list of two integer number, both <= 9
    return: string answer
    """
    print(f'{names[0]} matches {names[1]} {next_number_list[0]}{next_number_list[1]}%')


def main():
    names = get_names()
    names_loves = get_names_with_love(names)
    print('names_loves', names_loves)
    list_without_zero = get_list_of_numbers(names_loves)
    # print('list without zero', list_without_zero)
    # print('next_list_number', add_numbers_from_list(list_without_zero))
    next_number_list = add_numbers_from_list(list_without_zero)
    show_answer(names, next_number_list)


if __name__ == '__main__':
    main()


# names_loves = 'MarylovesJames'
# names_loves = names_loves.lower()
# print(names_loves)
# numbers = []
#
# for letter in names_loves:
#     numbers.append(names_loves.count(letter))
#     names_loves = names_loves.replace(letter, '')
#     print(names_loves)
#
#     # print(names_love[index])
#     # names_love = names_love.count(names_love[index])
# print('lista numerow', numbers)
#
# for index, number in enumerate(numbers):
#     if number == 0:
#         numbers.remove(number)
#         print(index, number)
#     continue
# print(numbers)
#
# list_without_zero = list(filter(lambda x: x != 0, numbers))
#
# print('lista numerow bez 0', list_without_zero)
#
# new_list = []
# while len(list_without_zero) >=1:
#     new_list.append(list_without_zero.pop(0)+list_without_zero.pop(-1))
# print('nowa lista', new_list)
#
# new_list2 = []
# while len(new_list) >= 1:
#     if len(new_list) != 1:
#         new_list2.append(new_list.pop(0)+new_list.pop(-1))
#     else:
#         new_list2.append(new_list.pop())
# print('nowa lista 2', new_list2)
#
# # while len(list_without_zero) >= 1:
# #     list_without_zero = list_without_zero.pop()
# # for number in list_without_zero:
# #     print(len(list_without_zero))
# #     list_without_zero = [list_without_zero[0] + list_without_zero[-1]]
#
# for number in numbers:
#     print('number', number)
#     print('numbers', numbers, len(numbers))
#     print('pop', numbers.pop(0), numbers.pop())
#
# print('lista', numbers)
#
# lista = [1, 1, 2]
# for i in lista:
#     lista.pop(0) + lista.pop()
# print(lista)
#
