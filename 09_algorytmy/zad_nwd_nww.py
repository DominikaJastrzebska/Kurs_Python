def nwd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def nww(a, b):
    return a * b / d


a = int(input('Podaj pierwsza liczbe: '))
b = int(input('Podaj druga liczbe: '))


d = nwd(a, b)
print(f'Najwieksza wspolna wielokrotnosc liczb {a} i {b} to:', nww(a, b),
      'a ich najmniejszy wspolny dzielnik to:', d)