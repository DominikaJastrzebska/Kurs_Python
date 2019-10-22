'''
1) Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach. Program powinen
wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
Napisz rozwiązanie zarówno z użyciem pętli while jak i for.
'''

print()
print('Rozwiazanie dla petli while')
print()

tempF = 0
while tempF <= 200:
    tempC = 5/9*(tempF-32)
    print(tempF, 'F = ', round(tempC,2), 'C')
    tempF = tempF + 20

print()
print('Rozwiazanie dla petli for')
print()

for tempF in range(0,201,20):
    tempC = 5 / 9 * (tempF - 32)
    print(tempF, 'F = ', round(tempC, 2), 'C')
