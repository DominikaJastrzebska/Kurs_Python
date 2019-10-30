import maxofthree as m3

def get_three_values():
  v1 = input('Podaj 1 liczbę całkowitą: ')
  v2 = input('Podaj 2 liczbę całkowitą: ')
  v3 = input('Podaj 3 liczbę całkowitą: ')
  return v1, v2, v3

if __name__ == "__main__":
  a, b, c = get_three_values()
  print(m3.maximum_of(a, b, c))