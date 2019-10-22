'''
5▹ Stwórz grę ciepło zimno.
1. Komputer losuje liczbę z zakresu od 1 do 100.
2. Użytkownik podaje swój traf.
3. Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
4. Jeśli użytkownik zgadnie wygrywa gracz.
5. Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.
'''

import random

comp_choice = random.randint(1, 100)
print(comp_choice)

for i in range(7):
    user_choice = int(input('Podaj liczbe 1-100: '))
    if comp_choice - 10 < user_choice < comp_choice + 10:
        if comp_choice != user_choice:
            print('Cieplo')
        else:
            print('Uzytkownik wygrywa')
            break
    else:
        print('Zimno')

if user_choice != comp_choice:
        print('Komputer wygrywa')
