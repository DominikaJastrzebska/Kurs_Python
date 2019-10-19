'''
7▹ Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w
krotce.
>>> example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
'''

print('Sposob 1: ')
example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

non_duplicte_list = []
for element in example_list:
    if element not in non_duplicte_list:
        non_duplicte_list.append(element)
print(non_duplicte_list)
example_list_to_tuple = tuple(non_duplicte_list)


print()
print('Sposob 2:')
example_list_2 = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
i = 0
while i < len(example_list_2):
    if example_list_2[i] in example_list_2[0:i]:
        example_list_2.remove(example_list_2[i])
    else:
        i += 1
print(example_list_2)

# for i in range(len(example_list)): #nie dziala
#     for j in range(len(example_list)):
#         if i !=j:
#             if example_list[i] == example_list[j]:
#                 example_list.remove(example_list[i])
# print(example_list)
