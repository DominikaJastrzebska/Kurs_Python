text = input('Podaj zdanie: ')

suma_low = 0
suma_title = 0
suma_sprcial = 0
for sign in text:
    if sign.islower():
        suma_low =