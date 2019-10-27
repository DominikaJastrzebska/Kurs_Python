from pprint import pprint

personal_data = {'person_1': {'name': 'Domi', 'surname': 'Jast', 'occupation': 'accountant', 'blood group': '0', 'mobile': '123 456 789'},
                 'person_2': {'name': 'Ala', 'surname': 'Kot', 'occupation': 'policewoman', 'blood group': 'B', 'mobile': '123 123 123'},
                 'person_3': {'name': 'Iwi', 'surname': 'Pirs', 'occupation': 'fireman', 'blood group': 'A', 'mobile': '456 456 456'},
                 'person_4': {'name': 'Darek', 'surname': 'Kuch', 'occupation': 'doctor', 'blood group': 'AB', 'mobile': '789 789 789'},
                 'person_5': {'name': 'Sara', 'surname': 'Jastrz', 'occupation': 'dancer', 'blood group': '0', 'mobile': '123 000 789'}}


activity = input('What do You want to do? show data - S, creating new data - C, deleting data - D, exit program - E')


def show_data():
    pprint(personal_data)
    print('All persons are: ')
    for person in personal_data:
        print()
        for el in personal_data[person]:
            print(personal_data[person][el], end=' ')


def creating_new_data():
    answer = input('What do you want to create? new person all index - A, one index - choose which one? '
                   'name - N, surname - S, occupation - O, blood group - B, mobile - M')
    if answer.lower() == 'a':
        personal_data['person_6'] ['name'] = input('Insert name: ')
        personal_data['person_6']['surname'] = input('Insert surname: ')
    print(personal_data)


if activity.lower() == 's':
    show_data()
elif activity.lower() == 'c':
    creating_new_data()

show_data()
print('lala')