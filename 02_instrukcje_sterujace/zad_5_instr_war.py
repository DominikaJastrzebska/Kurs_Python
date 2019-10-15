# password = input('Podaj haslo: ')
# if password.isalnum() == True:
#     if password.islower() == False:
#         if len(password) >=8:


# password = input('Podaj haslo: ')
# if password.isalnum() == False:
#     komunikat = 'Haslo nie sklada sie z samych liter i cyfr, wpisz poprawnie haslo, ' \
#                 'skladajace sie z liter i cyfr'
# elif password.islower() == True:
#     komunikat = 'Haslo nie zawiera co najmniej jednej duzej litery,' \
#                 ' wpisz haslo zawierajace co najmniej jedna duza litere'
# if len(password) <= 8:
#     komunikat = 'Haslo jest za krotkie, wpisz haslo, ktore zawiera co najmnie 8 znakow'
# print(komunikat)


password = input('Gimme password: ' )
alphanum = password.isalnum()
condition_only_lower = alphanum and password.islower()

if len(password) <8:
    print('Password is too short. Should be 8 chars')
if not alphanum:
    print('Your pass should be alphanumeric')
if password.isalpha():
    print('Should contain digits too')
if password.isdigit():
    print('Should contain letters too')
if condition_only_lower:
    print('Should contain at least one upper')
print('End')

