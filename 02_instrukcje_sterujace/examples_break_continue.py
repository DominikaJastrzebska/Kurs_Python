'''
Chcemy znaleźć liczby pierwsze, w tym celu potrzebujemy 2 pętli for:
'''

for current_num in range(2, 10):
    for x in range(2, current_num):
        if current_num % x == 0:
            print(current_num, 'equals', x, '*', current_num // x)
            # znaleziono dzielnik!!! - możemy przejść do kolejnej cuurrent_num
            # pomijając sprawdzanie x
            break
        else:
            # nie znaleziono dzielnika
            print(current_num, 'can\'t be divided by', x)

print('-------------')
for val in "string":
    if val == "i":
        break
    print(val)
print("Koniec")
print('--------------')

for val in "string":
    if val == "i":
        print('lalala')
        continue
    print(val)
print("Koniec")

print('---------------')
for val in "string":
    if val == "i":
        print('lalala')
    print(val)
print("Koniec")