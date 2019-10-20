'''
3▹ Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie
tabeli n x n. Elementy powinny być oddzielone spacją
wejście:
n = 3
tab = [['-', '-', '-']
['-', '-', '-'],
['-', '-', '-']]
wyjście:
- - -
- - -
- - -
'''

tab = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

for row in range(len(tab)):
    print()
    for col in range(len(tab[row])):
        print(tab[row][col], end=' ')
print()
print('--------------------------')
print()
print('Wersja rozszerzona: ')
dim_row = int(input('Podaj wymiar wierszy: '))
dim_col = int(input('Podaj wymiar kolumn: '))
tabl = []
#el = input('Podaj element, ktory bedzie dodany do tablicy: ')
for row in range(dim_row):
    tabl_row = []
    for col in range(dim_col):
        tabl_row.append(input('Podaj element {0}, {1} macierzy: '.format(row+1, col+1)))#jak zrobic tutaj indeksacje?
    tabl.append(tabl_row)
print(tabl)

for row in range(len(tabl)):
    print()
    for col in range(len(tabl[row])):
        print(tabl[row][col], end=' ')



