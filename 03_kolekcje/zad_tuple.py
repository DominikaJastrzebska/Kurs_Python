'''
Zadanie do przeanalizowania:
▹ Policz elementy na liście, dopóki element nie będzie krotką.
numbers = [1, 2, 3, (10, 20), 4, 5]
'''

# numbers = [1, 2, 3, (10, 20), 4, 5]
# counter = 0
# for n in numbers:
#     print(n)
#     if isinstance(n, tuple):  #type(numbers[n.index()]) is not tuple:
#         break
#     counter +=1
#     print('Wynik', counter)
#
# print(type((10, 20)))

numbers = [1, 2, 3, (10, 20), 4, 5]
counter = 0
for n in numbers:
    print(n)
    if type(n) is tuple:
    #if type(n) == <class 'tuple'>:  #type(numbers[n.index()]) is not tuple:
        break
    counter +=1
    print('Wynik', counter)
