def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""
    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(4))
print(absolute_value(-5))


def greet(name):
    print('Good morning!', name)
    return


print(greet('Vicky'))


def greet(name):
    print('Good morning!', name)


print(greet('Vicky'))