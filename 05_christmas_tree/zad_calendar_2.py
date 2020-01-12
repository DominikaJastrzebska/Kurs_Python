

def add_zero(value):
    if value < 10:
        return '0' + str(value)
    else:
        return str(value)


def show_calendar():
    for month in data:
        print(month[0])

        for day in month[1]:
            if day % 7 == 0:
                print()
                print(add_zero(day), end=' ')
            else:
                print(add_zero(day), end=' ')

        print('\n---------------------')


# glowna czesc programu
data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
]

show_calendar()
