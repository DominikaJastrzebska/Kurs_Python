'''
3▹ Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni
element są takie same.
'''

# print('Sposob 1: ')
#
# lista_liczb = []
# counter = int(input('Ile liczb chcesz dodac? '))
# for i in range(counter):
#     liczba = int(input('Podaj liczbe: '))
#     lista_liczb.append(liczba)
# print(lista_liczb)
#
# if lista_liczb[0] == lista_liczb[len(lista_liczb)-1]:
#     komunikat = 'Pierwszy i ostatni element listy sa takie same.'
# else:
#     komunikat = 'Pierwszy i ostatni element listy nie sa takie same'
#
# print(komunikat)
#
# print('------------------------------')

# print('Sposob 2:')
# counter = int(input('Ile liczb chcesz dodac?: '))
# elements = []
# for _ in range(counter):
#     e = input('Podaj element: ')
#     elements.append(e)
# print(elements)
#
# print('Czy pierwszy i ostatni sa takie same:', elements[0] ==elements[-1])
#
# if elements[0] == elements[-1]:
#     print('Pierwszy i ostatni sa takie same')
# else:
#     print('Elementy nie sa takie same')

# print('------------------')
# print('Sposob 3:')
#
# elements2 = []
# counter2 = 5
# while counter2 > 0:
#     e = input('Podaj elementy: ')
#     elements2.append(e)
#     counter2 -= 1
# if elements2[0] == elements2[-1]:
#     print('Pierwszy i ostatni element sa takie same.')
# else:
#     print('Pierwszy i ostatni element nie sa takie same')
# print(elements2)

print('--------------------')
print('Sposob 4:')

num_arr = []
while True:
    e = input('Podaj nowy element. Nacisnij Q aby zakonczyc: ')
    if e == 'Q':
        break
    num_arr.append(e)

print(num_arr)

if num_arr[0] == num_arr[-1]:
    print('Pierwszy i ostatni element sa takie same.')
else:
    print('Pierwszy i ostatni element nie sa takie same.')

