# from pprint import pprint
# lista_osob = [['Dorota', 'Wellman', 'dziennikarka'], ['Adam', 'Malysz', 'sportowiec'],
#               ['Robert', 'Lewandowski', 'pilkarz'], ['Krystyna', 'Janda', 'aktorka']]
#
# for i in range(4):
#     for j in range(4):
#         print(lista_osob[i])
#
# print('---------')
# pprint(lista_osob)

people = [
    ['Dorota', 'Wellman', 'dziennikarka', 'pies'],
    ['Adam', 'Malysz', 'sportowiec', 'kot'],
    ['Robert', 'Lewandowski', 'pilkarz'],
    ['Krystyna', 'Janda', 'aktorka']
]

for row in people:
    print(row[0], row[1], '-', row[2])

print('----------------------------')

print('Liczba ludzi', len(people))

for row in range(len(people)):
    print() #print(end=\n\n)
    for col in range(len(people[row])):
        #print(people[row][col], end=' ')
        if col == 1:
            print(people[row][col], end=' - ')
        elif col == 2:
            print(people[row][col], end = ' * ')
        else:
            print(people[row][col], end=' ')
