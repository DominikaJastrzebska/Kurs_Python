'''
lista_liczb = []
counter = int(input('Ile liczb chcesz dodac?'))
for i in range(counter):
    liczba = int(input('Podaj liczbe: '))
    lista_liczb.append(liczba)
print(lista_liczb)

if lista_liczb[0] == lista_liczb[len(lista_liczb)-1]:
    komunikat = 'Pierwszy i ostatni element listy sa takie same.'
else:
    komunikat = 'Pierwszy i ostatni element listy nie sa takie same'

print(komunikat)
'''

# counter = int(input('Ile liczb chcesz dodac?: '))
# elements = []
# for _ in range(counter):
#     e = input('Podaj element: ')
#     elements.append(e)
# print(elements)
#
# print('Czy pierwszy i ostatni sa takie same:', elements[0] ==[-1])
#
# if elements[0] == elements[-1]:
#     print('Pierwszy i ostatni sa takie same')
# else:
#     print('Elementy nie sa takie same')

# elements2 = []
# counter2 = 5
# while counter2 > 0:
#     e = input()
#     elements2.append(e)
#     counter2 -= 1
# print(elements2)

num_arr = []
while True:
    e = input('Podaj nowy element. Nacisnij Q aby zakonczyc: ')
    if e == 'Q':
        break
    num_arr.append(e)

print(num_arr)