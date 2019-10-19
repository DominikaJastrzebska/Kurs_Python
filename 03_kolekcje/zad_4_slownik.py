'''
4▹ Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami
mnożenia wiersz × kolumna.
'''


tabl = []
for row in range(1, 11):
    tabl_row = []
    for col in range(1, 11):
        tabl_row.append(row * col)
    tabl.append(tabl_row)
print(tabl)

for row in range(len(tabl)):
    print()
    for col in range(len(tabl[row])):
        if len(str(row * col)) == 2:
            print(tabl[row][col], end=' ' * (int(len(str(row * col))) + 1))
        elif len(str(row * col)) == 1:
            print(tabl[row][col], end=' ' * (int(len(str(row * col))) + 3)) #odleglosci??

# print(len(str(10)))
# print(len(tabl[row]))
# for row in range(len(tabl)):
#     print()
#     for col in range(len(tabl[row])):
#         print(row, col, row*col, len(str(row*col)))

print()

for row in range (1, 11):
    print()
    for col in range(1, 11):
        if row * col < 10:
            print(row * col, end=' ' * 4)
        else:
            print(row * col, end=' ' * 3)