import math


def circle_field(radius):
    pi = 3.14
    return pi * radius **2


r = float(input('Podaj promien kola: '))
p_circle = circle_field(r)
print(p_circle)


