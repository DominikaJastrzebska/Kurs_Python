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

# card_number = input('Podaj nr karty: ')
# if int(card_number[0]) == 4:
#     if len(card_number) == 16:
#         print('Visa new')
#     else:
#         print('Visa old')
# elif card_number[0:2] in range(51, 56) or card_number[0:1] in range(2221, 2721):
#     if len(card_number) == 16:
#         print('MasterCard')
# elif card_number[0:2] in (34, 37):
#     if len(card_number) == 15:
#         print('American Express')
#     else:
#         print('Nie Am')
#
# print((card_number[0:2]))

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


#Visa
#All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
# visa 4944646029104842

if can_be_card_number and (len(card_number) == 16 or len(card_number) == 13):
    if card_number[0] == '4':
        print('Your card is Visa!')

#Mastercard
#MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through
#2720. All have 16 digits.
# master 5255269264057995

if can_be_card_number and len(card_number) == 16:
    if int(card_number[0:2]) in range(51, 56) or int(card_number[0:4]) in range(2221, 2721):
        print("I'm master card")


#American Express
# American Express card numbers start with 34 or 37 and have 15 digits.
# american 341767854473560

if can_be_card_number and len(card_number) == 15:
    if card_number[0:2] in ('34', '37'):
        print("I'm american express")