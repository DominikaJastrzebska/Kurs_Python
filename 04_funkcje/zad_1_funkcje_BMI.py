'''
1▹ Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą
bmi na podstawie danych użytkownika oraz zwracającą odpowiednią wartość
(niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.
'''


def calc_bmi(weight, height):
    return weight / height ** 2


def bmi_status(bmi):
    if bmi < 19:
        print('Niedowaga')
    elif bmi < 25:
        print('Waga normalna')
    elif bmi < 30:
        print('Nadwaga')
    else:
        print('Otylosc')


h = 1.60
w = 60

bmi = round(calc_bmi(w, h), 4)
print(bmi)
bmi_status(bmi)
