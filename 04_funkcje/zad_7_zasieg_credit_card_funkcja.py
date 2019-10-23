'''
7▹ Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a
może AmericanExpress.
Co wiemy o tych numerach tych kart?
All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through
2720. All have 16 digits.
American Express card numbers start with 34 or 37 and have 15 digits.
'''
'''
https://ccardgenerator.com/generat-visa-card-numbers.php

'''
# visa 4944646029104842
# master 5255269264057995
# american 341767854473560

# teraz przerabiamy na funkcje zad z kartami


def is_visa(is_card, number):
    # Visa
    # All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
    # visa 4944646029104842
    if not is_card:
        return False

    if len(number) == 16 or len(number) == 13:
        if number[0] == '4':
            return True


def is_mastercard(is_card, number):
    # Mastercard
    # MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through
    # 2720. All have 16 digits.
    # master 5255269264057995
    if not is_card:
        return False

    if len(number) == 16:
        if int(number[0:2]) in range(51, 56) or int(number[0:4]) in range(2221, 2721):
            return True


def is_american_express(is_card, number):
    # American Express
    # American Express card numbers start with 34 or 37 and have 15 digits.
    # american 341767854473560
    if not is_card:
        return False
    if len(number) == 15:
        if number[0:2] in ('34', '37'):
            return True


card_number = input('Put your card number here: ')
can_be_card_number = False

if len(card_number) < 13 or len(card_number) > 16:
    print('Wrong number')
else:
    if card_number.isdecimal():
        print('Can be a card number')
        can_be_card_number = True
    else:
        print('Not a number')


if is_visa(can_be_card_number, card_number):
    print("I'm Visa")
elif is_mastercard(can_be_card_number, card_number):
    print("I'm MasterCard")
elif is_american_express(can_be_card_number, card_number):
    print("I'm american express")
else:
    print('Not known number card')