'''
6▹ Wywołaj błąd związany z otwarciem pliku.
Spróbuj odczytać plik, który nie istnieje.
Spróbuj odczytać wartość z pliku otwartym w trybie w
Spróbuj utworzyć plik, który już istnieje w trybie x
Obsłuż w dowolny sposób każdy z powyższych błędów.
'''

filename = 'text.txt'
try:
    with open(filename, 'r') as f:
        f.read()
except FileNotFoundError as e:
    print(e)

filename2 = 'text2.txt'
try:
    with open(filename2, 'w') as f:
        f.read()
except Exception as e:
    print(e)

try:
    with open(filename2, 'x') as f:
        f.write()
except FileExistsError as e:
    print(e)