'''
1▹ Utwórz listę lists_to_dict zawierającą listy 2 elementowe. Przekształć ją w słownik
dict_from_list.
'''

from pprint import pprint

list_to_dict = [
    ['apple', 'jablko'],
    ['pear', 'gruszka'],
    ['cherry', 'wisnie']
]

dict_from_list = dict(list_to_dict)

pprint(dict_from_list)
