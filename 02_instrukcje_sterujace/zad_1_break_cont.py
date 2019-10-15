imiona = input('Podaj imiona rozdzielone przecinkiem lub spacja: ')

imiona = imiona.split(' ')

for imie in imiona:
    print('Hello', imie)
print('----------------')

id = 0
while id < len(imiona):
    print("Hi", imiona[id])
    id = id + 1

