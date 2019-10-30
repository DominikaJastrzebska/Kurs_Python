def triangle_field(base, height):
    result = 1/2 * base * height
    return result


def circle(radius):
    result = 3.14 * radius ** 2
    return result


def square(base):
    result = base ** 2
    return result


def rectangle(base_a, base_b):
    result = base_a * base_a
    return result


def main():
    print(square(9))


if __name__ == '__main__':
    main()
else:
    print('Modul zaimportowany')