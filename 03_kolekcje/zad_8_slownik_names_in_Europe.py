'''
8.
Slowniki dla 10 krajów Europy utwórz listy 10 najpopularniejszych imion zenskich. Za kazdym razem
zapisz imiona w wersji anglojezycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierac 100
elementów.
Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.
'''

names_dict = {
    'PL': ['Ann', 'Sarah', 'Gabriel', 'Olivier', 'Harry', 'George', 'Jacob', 'Sofia', 'Emily', 'Julia'],
    'EN': ['Noah', 'Jake', 'Jacob', 'Ann', 'Sarah', 'Leo', 'Olivier', 'Amelia', 'Emily', 'Olivia'],
    'DE': ['Sarah', 'Oscar', 'Gabriel', 'Leo', 'Harry', 'Margaret', 'Emma', 'Emilia', 'Hannah', 'Marie'],
    'FL': ['Elen', 'Emma', 'Emilia', 'Edith', 'Sofia', 'Elsa', 'Olivier', 'Robert', 'Oscar', 'Henri'],
    'DK': ['Noah', 'Victor', 'Oliver', 'Oscar', 'William', 'Lucas', 'Carl', 'Sofia', 'Elsa', 'Emma'],
    'FR': ['Emma', 'Alice', 'Rose', 'Lea', 'Marie', 'Gabriel', 'Adam', 'Lucas', 'Leo', 'Hugo'],
    'IT': ['Gabriel', 'Leo', 'Rose', 'Lea', 'Marie', 'Sofia', 'Alice', 'Emma', 'Ann', 'Julia'],
    'LX': ['Emma', 'Lara', 'Sarah', 'Emily', 'Sofia', 'Gabriel', 'Leo', 'David', 'Luca', 'Tom'],
    'MT': ['Luca', 'Jacob', 'John', 'Ben', 'Tom', 'Julia', 'Emma', 'Elsa', 'Kate', 'Lea'],
    'MD': ['Sofia', 'Victoria', 'Amelia', 'Andrea', 'David', 'Daniel', 'Gabriel', 'Michael', 'Bogdan', 'Maxim'],
}

names_list = []
for key, value in names_dict.items():
    for names in value:
        names_list.append(names)
print(len(names_list))

names_q_dict = {}
for name in names_list:
    if name in names_q_dict:
        names_q_dict[name] += 1
    else:
        names_q_dict[name] = 1
print(names_q_dict)

for key, value in names_q_dict.items():
    if value > 2:
        print(key, value)
