'''
6. Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę
wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.
'''

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
