'''
2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
'''

even_number_list = []
odd_number_list = []

for i in range(10):
    number = int(input('Podaj liczbe calkowita: '))
    if number % 2 == 0:
        even_number_list.append(number)
    else:
        odd_number_list.append(number)

print('Liczby parzyste: ', even_number_list)
print('Liczby nieparzyste: ', odd_number_list)

