'''
3▹ W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery,
cyfry i znaki specjalne.
'''

text = input('Podaj zdanie: ')

sum_low = 0
sum_title = 0
sum_special = 0
sum_digits = 0
for sign in text:
    if sign.islower():
        sum_low += 1
    elif sign.istitle():
        sum_title += 1
    elif sign.isdigit():
        sum_digits += 1
    else:
        sum_special = len(text) - sum_digits - sum_title - sum_low
print('Male litery: ', sum_low)
print('Duze litery', sum_title)
print('Cyfry: ', sum_digits)
print('Znaki specjalne: ', sum_special)