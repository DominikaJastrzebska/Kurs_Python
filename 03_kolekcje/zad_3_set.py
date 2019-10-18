'''
3▹ Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z
pierwszej krotki, a oraz nieparzystych elementów z drugiej.
'''

tuple_1 = tuple('ala''ma''kota''356')
tuple_2 = tuple('tra''ta''ta''23''35')
print(tuple_1)
print(tuple_2)

tuple_1_to_list = list(tuple_1)
tuple_2_to_list = list(tuple_2)

print(tuple_1_to_list)
print(tuple_2_to_list)

even_el = []
odd_el = []
for index, element in enumerate(tuple_1_to_list):
    if index % 2 == 0:
        even_el.append(element)
print('Lista parzystych elementow: ',even_el)
for index, element in enumerate(tuple_2_to_list):
    if index % 2 != 0:
        odd_el.append(element)
print('Lista niearzystych elementow: ', odd_el)

print(even_el+odd_el)

# list_number = [0, 1, 2, 3, 4, 4, 4, 5, 'x']
# for element in list_number:
#     print(list_number.index(element), element)
