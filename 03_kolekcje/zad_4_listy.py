'''
4▹ Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.
'''

print('Sposob 1:')
print()

elements_list = []

while True:
    element = input('Podaj element. Aby zakonczyc, wcisnij Q ')
    if element == 'Q':
        if len(elements_list) % 2 == 0:
            break
        else:
            print('Wymagana parzysta liczba elementow. Podaj jeszcze jeden element: ')
            element = input()
            elements_list.append(element)
            break
    elements_list.append(element)

print('Lista elementow: ', elements_list)

lenght = len(elements_list)

print('Dlugosc listy: ', lenght)
print('---------')
print('element 3:', elements_list[2], 'element 4: ', elements_list[3])

if elements_list[int(lenght/2-1)] == elements_list[int(lenght/2)]:
    print('Srodkowe elementy sa takie same')
else:
    print('Srodkowe elementy sa rozne.')
print('x: ',elements_list[int(lenght/2-1)])
print('y: ', elements_list[int(lenght/2)])

# print('----------------------------------')
# print('Sposob 2:')
# print()
# elements_list = []
#
# while True:
#     element = input('Podaj element. Aby zakonczyc, wcisnij Q ')
#     if len(elements_list) % 2 == 0:
#         if element == 'Q':
#             break
#     else:
#         if element == 'Q':
#             print('Podaj jeszcze jeden element')
#             element = input()
#             elements_list.append(element)
#             break
#     elements_list.append(element)
#
# print('Lista elementow: ', elements_list)
#
# lenght = len(elements_list)
#
# print('Dlugosc listy: ', lenght)
# print('---------')
# print('element 3:', elements_list[2], 'element 4: ', elements_list[3])
#
# if elements_list[int(lenght/2-1)] == elements_list[int(lenght/2)]:
#     print('Srodkowe elementy sa takie same')
# else:
#     print('Srodkowe elementy sa rozne.')
# print('x: ',elements_list[int(lenght/2-1)])
# print('y: ', elements_list[int(lenght/2)])