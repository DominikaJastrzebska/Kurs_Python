'''
6▹ Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.
'''

import random

# comp_choice = random.choice(['k', 'p', 'n'])
# print(comp_choice)
# dict_of_wins = {'kamien':'nozyce', 'papier':'kamien', 'nozyce': 'papier'}
DICT_OF_WINS = {'k':'n', 'p':'k', 'n':'p'} # konwencja stale w pythonie
# user_choice = input('Podaj, co wybierasz: k - kamien, p - papier, n - nozyce: ')


def figure_choose():
    comp_choice = random.choice(['k', 'p', 'n'])
    user_choice = input('Podaj, co wybierasz: k - kamien, p - papier, n - nozyce: ')
    # print(user_choice)
    print('Komputer wybral:', comp_choice)
    return comp_choice, user_choice


def who_wins(comp_choice, user_choice):
    # comp_choice, user_choice = figure_choose()
    # comp_choice = random.choice(['k', 'p', 'n'])
    # print(comp_choice)
    # user_choice = input('Podaj, co wybierasz: k - kamien, p - papier, n - nozyce: ')
    if user_choice == comp_choice:
        print('Remis')
    elif DICT_OF_WINS[user_choice] == comp_choice:
        print('Uzytkownik wygrywa')
    else:
        print('Komputer wygrywa')
    play_again()


def play_again():
    question = input('Chcesz zagrac jeszcze raz? y/n ')
    while True:
        if question.lower() == 'y':
            comp_choice, user_choice = figure_choose()
            who_wins(comp_choice, user_choice)
        else:
            exit()


comp_choice, user_choice = figure_choose()
who_wins(comp_choice, user_choice)
play_again()
