'''
2) Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np.
secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.
'''

hidden_number = 37

while True:
    user_number = int(input('Podaj liczbe w przedziale od 1 do 100: '))
    if user_number == hidden_number:
        message = 'Gratulacje'
        break
    else:
        message = 'Pudlo, zdaguj dalej'
        print(message)
        continue

print(message)