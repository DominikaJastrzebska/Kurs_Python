'''
9.
5 uzytkowników popros o podanie 4 przedmiotów szkolnych, sprawdz czy przedmioty powtarzaja sie
na listach. Wyswietl najpopularniejszy przedmiot. (Uwzglednij fakt, ze uzytkownicy moga zapisac
przedmioty malymi, drukowanymi lub zaczynajac od duzej litery)
'''

user_list = []
for user in range(1, 3): #zmienic na range(1, 6)
    subject_list = []
    print(('Uzytkownik %d podaje przedmioty: ') %(user))
    for sub in range(1, 3):
        subject = input('Podaj przedmiot: ')
        subject_list.append(subject)
    user_list.append(subject_list)
print(user_list)

subject_dict = {}
for subject_list in user_list:
    for subject in subject_list:
        if subject.lower() not in subject_dict:
            subject_dict[subject.lower()] = 1
        else:
            subject_dict[subject.lower()] += 1
print(subject_dict)

for items in subject_dict:
    print(subject_dict.items())
    if subject_dict.values() == max(subject_dict.values()):
        print(subject_dict.items())
        print(max(subject_dict.values()))
print(max(subject_dict.values()))