'''
5▹ Napisz grę ciepło - zimno tak, aby korzystać z funkcji.
'''

import random


def main():
    guess_game()
    try_again()


def guess_game():
    number = random.randint(0, 100)
    print(number)
    guess_taken = 0
    while guess_taken < 10:
        guess = int(input('Podaj liczbe 0-100: '))
        if number - 10 < guess < number + 10 and number != guess:
            print('Cieplo')
        elif guess == number:
            print('Wygrales')
            break
        else:
            print('Zimno')
        guess_taken += 1
    try_again()


def try_again():
    again = input('Chcesz zagrac jeszcze raz? ')
    if again.lower() == 'y':
        guess_game()
    else:
        exit()


guess_game()

