'''
2▹ Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).
'''

text = input('Podaj dowolny ciag znakow: ')
dl = len(text)
print(str(text[1:dl+1:2]))

print('*******************')

for sign in text:
    if (text.index(sign)+1) % 2 == 0:
        print(sign, end="")
    else:
        continue

print('\n-----------------')

i = 0
while i < len(text):
    print(text[i+1], end='')
    i = i + 2
