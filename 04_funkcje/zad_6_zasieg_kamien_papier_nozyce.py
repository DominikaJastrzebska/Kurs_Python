'''
6▹ Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.
'''

import random

comp_choice = random.choice(['k', 'p', 'n'])
print(comp_choice)
user_choice = input('Podaj, co wybierasz: k - kamien, p - papier, n - nozyce: ')
#dict_of_wins = {'kamien':'nozyce', 'papier':'kamien', 'nozyce': 'papier'}
DICT_OF_WINS = {'k':'n', 'p':'k', 'n':'p'} #konwencja stale w pythonie

def who_wins(comp, user):
    if user_choice == comp_choice:
        print('Remis')
    elif DICT_OF_WINS[user_choice] == comp_choice:
        print('Uzytkownik wygrywa')
    else:
        print('Komputer wygrywa')


who_wins(comp_choice, user_choice)
