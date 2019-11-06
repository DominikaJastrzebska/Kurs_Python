# dom szkola kosciol bar szpital kino teatr

# macierz = [
#     [0, 1, 2, 3, 0, 0, 0],
#     [1, 0, 0, 0, 1, 0, 0],
#     [1, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 0, 1, 0, 0],
#     [0, 1, 0, 1, 0, 1, 1],
#     [0, 0, 1, 0, 1, 0, 1],
#     [0, 0, 0, 0, 1, 1, 0]
# ]
#
# for row in range(len(macierz)):
#     for col in range (len(macierz[row])):
#         if macierz[row][col] == 1:
#             print(row,'---', col)

lista_obiektow = ['dom', 'szkola', 'kosciol', 'bar', 'szpital', 'kino', 'teatr']
                    #0      1           2       3       4           5       6
#
# graph = [(0, 1), (0, 2), (0, 3), (1, 4), (2, 3)]
# for i in graph:
#     b1, b2 = i
#     print(lista_obiektow[b1], '---', lista_obiektow[b2])

graph = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1]
]

for row in range(4):
    for col in range(5):
        if graph[row][col] == 1:
            print(lista_obiektow[row], '<--->', lista_obiektow[col])