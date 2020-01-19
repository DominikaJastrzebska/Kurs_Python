def create_board():
    # print('  A', '  B  ', 'C', end=' ')
    print()
    for i in range(0, 4):
        if i == 0:
            print('  A', '  B  ', 'C', end=' ')
            print()
        else:
            print(i, end=' ')
        for j in range(3):
            if i == 0:
                pass
            else:
                if j < 2:
                    print('. | ', end='')
                else:
                    print('.')


def who_wins():
    pass


create_board()