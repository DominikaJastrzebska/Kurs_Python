'''
7. Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w
zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.
'''

weight = float(input('Podaj wage w kg: '))
height = float(input('Podaj wzrost w cm: '))

BMI = weight/(height/100)**2
print(round(BMI,2))

if BMI < 20:
    infrmation = 'niedowaga'
elif 20 <= BMI <= 25:
    information = 'waga w normie'
elif 25 < BMI <= 29:
    information = 'lekka nadwaga'
elif 29 < BMI <= 37:
    information = 'nadwaga'
else:
    information = 'otylosc'

print('Twoje BMI wynosi', str(round(BMI, 2)) + ', diagnoza:', information)
