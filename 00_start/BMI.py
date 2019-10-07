name = input('Podaj swoje imie: ')
weight = float(input('Podaj wage: '))
height = float(input('Podaj wzrost w metrach: '))

BMI = weight/height**2

print(name + ', twoje BMI wynosi', str(round(BMI, 2)))
