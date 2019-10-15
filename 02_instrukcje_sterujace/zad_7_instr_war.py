weight = float(input('Podaj wage w kg: '))
height = float(input('Podaj wzrost w cm: '))

BMI = weight/(height/100)**2
print(round(BMI,2))

if BMI < 20:
    komunikat = 'niedowaga'
elif 20<= BMI <=25:
    komunikat = 'waga w normie'
elif 25 <BMI <=29:
    komunikat = 'lekka nadwaga'
elif 29 < BMI <=37:
    komunikat = 'nadwaga'
else:
    komunikat = 'otylosc'
print('Twoje BMI wynosi', str(round(BMI, 2)) + ', diagnoza:', komunikat)