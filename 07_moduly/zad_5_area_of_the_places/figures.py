def triangle(base, height):
    return 0.5 * base * height


def rectangle (base_a, base_b):
    return base_a * base_a


def square(base):
    return base ** 2


def parallelogram(base, height): # rownoleglobok
    return base * height


def diamond(base, height):
    return base * height


def trapeze(base_a, base_b, height):
    return 0.5 * (base_a + base_b) * height


def circle(radius):
    return 3.14 * radius ** 2


def main():
    print(square(2))


if __name__ == '__main__':
    main()
else:
    print('Modul zaimportowany')