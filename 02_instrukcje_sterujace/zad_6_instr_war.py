hidden_number = 37

while True:
    user_number = int(input('Podaj liczbe w przedziale od 1 do 100: '))
    if user_number == hidden_number:
        komunikat = 'Gratulacje'
        break
    else:
        komunikat = 'Pudlo, zdaguj dalej'
        print(komunikat)
        continue
print(komunikat)