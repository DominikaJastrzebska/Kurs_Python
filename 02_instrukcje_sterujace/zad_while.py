#popros uzytkownika o podanie 3 przedmiotow oraz ocene jaka z nich uzyskal
# i wyswietl jaka uzywkal ocene

# i = 0
# while i < 3:
#     subject = input('Podaj przedmiot: ')
#     grade = input('Podaj ocene: ')
#     i = i + 1
# print(subject + ': ' + grade)

# p = 1
# while (p<=3):
#     przed = input('Podaj przed: ')
#     grade = input('Podaj ocene: ')
#     print(przed, "-", grade)
#     print('Aktualny przedmiot', p)
#     p = p+1

przedmioty = input('Podaj przedmioty podzielone myslnikiem: ')
oceny = input('Podaj oceny podzielone myslnikiem: ')
przedmioty = przedmioty.split('-')
print(przedmioty)
print(oceny)

licznik = 0
while licznik < 3:
    print(przedmioty[licznik], oceny[licznik])
    licznik = licznik + 1
