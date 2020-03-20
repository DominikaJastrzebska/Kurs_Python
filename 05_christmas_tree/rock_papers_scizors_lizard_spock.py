import random

# comp_choice = random.choice(['k', 'p', 'n'])
# print(comp_choice)
# dict_of_wins = {'kamien':'nozyce', 'papier':'kamien', 'nozyce': 'papier', }
DICT_OF_WINS = {'k':'n', 'p':'k', 'n':'p'} # konwencja stale w pythonie

# dict_of_wins = {
# 'kamien':['nozyce', 'jaszczurka'],
# 'papier':['kamien', 'spock'],
# 'nozyce': ['papier', 'jaszczurka'],
# 'jaszczurka': ['papier', 'spock'],
# 'spock: ['kamien', 'nozyce']}
DICT_OF_WINS_DIFFICULT = {'k': ['n', 'j'],
                          'p': ['k', 's'],
                          'n': ['p', 'j'],
                          'j': ['p', 's'],
                          's': ['k', 'n']}

print()
# user_choice = input('Podaj, co wybierasz: k - kamien, p - papier, n - nozyce: ')

comp_wins = 0
user_wins = 0
dead_heat = 0
rounds = 0
statistic = []


def menu():
    print('Welcome:\n'
          'S - Start\n'
          'P - Difficulty level\n'
          'Q - Quit\n')
    choice_option = input('Please choose the option: ')
    print()
    return choice_option


def main():
    play = True
    while play:
        option = menu()
        if option.upper() == 'S':
            comp_choice, user_choice = figure_choose()
            who_wins(comp_choice, user_choice)
        elif option.upper() == 'P':
            comp_choice, user_choice = figure_choose_difficult()
            who_wins_difficult(comp_choice, user_choice)
        elif option.upper() == 'Q':
            get_statistic()
            quit()
        else:
            print('Wrong option, please put correct option:')


def figure_choose():
    comp_choice = random.choice(['k', 'p', 'n'])
    user_choice = input('Podaj, co wybierasz: k - kamien, p - papier, n - nozyce: ')
    # print(user_choice)
    print('Komputer wybral:', comp_choice)
    return comp_choice, user_choice


def figure_choose_difficult():
    comp_choice = random.choice(['k', 'p', 'n', 'j', 's'])
    user_choice = input('Podaj, co wybierasz: k - kamien, p - papier, n - nozyce, j - jaszczurka, s - spock: ')
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
        statistic.append('R')
        print('r', statistic)
    elif DICT_OF_WINS[user_choice] == comp_choice:
        print('Uzytkownik wygrywa')
        statistic.append('U')
        print('u', statistic)
    else:
        print('Komputer wygrywa')
        statistic.append('K')
        print('k', statistic)
    play_again()


def who_wins_difficult(comp_choice, user_choice):
    # comp_choice, user_choice = figure_choose()
    # comp_choice = random.choice(['k', 'p', 'n'])
    # print(comp_choice)
    # user_choice = input('Podaj, co wybierasz: k - kamien, p - papier, n - nozyce: ')
    if user_choice == comp_choice:
        print('Remis')
        statistic.append('R')
    elif comp_choice in DICT_OF_WINS_DIFFICULT[user_choice]:
        print('Uzytkownik wygrywa')
        statistic.append('U')
    else:
        print('Komputer wygrywa')
        statistic.append('K')
    play_again()


def play_again():
    question = input('Chcesz zagrac jeszcze raz? y/n ')
    while True:
        if question.lower() == 'y':
            statistic.append('round_number')
            main()
            # comp_choice, user_choice = figure_choose()
            # who_wins(comp_choice, user_choice)
        else:
            get_statistic()
            exit()


def get_statistic():
    k = statistic.count('K')
    u = statistic.count('U')
    r = statistic.count('R')
    round_number = statistic.count('round_number')
    print('komputer -', k, ',', 'uzytkownik -', u, ',', 'remis - ', r, ',', 'liczba rund -', round_number + 1)


# for i in statistic:
#     k = statistic.count('K')
#     u = statistic.count('U')
#     r = statistic.count('R')
# print(k, u, r)
print(statistic.count('U'))
print('statystyka:', statistic)
# def statistics(user_wins, comp_wins, dead_heat, rounds):
#     return user_wins, comp_wins, dead_heat, rounds


main()
# comp_choice, user_choice = figure_choose()
# who_wins(comp_choice, user_choice)
play_again()


