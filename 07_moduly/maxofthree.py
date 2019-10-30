def max_of_2(x, y):
  return x if x > y else y


def maximum_of(num1, num2, num3):
    return max_of_2(max_of_2(num1, num2), num3)


if __name__ == "__main__":
  a, b, c = (4, 12, 7)
  v = maximum_of(a, b, c)
  print("Moja wieksza liczba to: ", v)