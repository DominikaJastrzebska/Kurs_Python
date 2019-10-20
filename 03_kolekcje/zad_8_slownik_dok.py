'''
8.
Slowniki dla 10 krajów Europy utwórz listy 10 najpopularniejszych imion zenskich. Za kazdym razem
zapisz imiona w wersji anglojezycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierac 100
elementów.
Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.
'''

names_dict = {
    'PL':['Ann', 'Sarah', 'Gabriel', 'Olivier', 'Harry', 'George'],
    'EN':['Noah', 'Jake', 'Jacob', 'Ann', 'Sarah', 'Leo'],
    'DE':['Sarah', 'Oscar', 'Gabriel', 'Leo', 'Harry', 'Margaret']
}

names_list = []
for key, value in names_dict.items():
    for names in value:
        names_list.append(names)

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
