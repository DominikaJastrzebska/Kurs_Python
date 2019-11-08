'''
4▹ Napisz grę - kamień (k) / papier (p) / nożyce (n).
1. Użytkownik podaje jedną z 3 figur.
2. Komputer losuje jedną z 3 figur.
3. Sprawdź kto wygrał tę rundę.
4. Zmień kod tak, by użytkownik mógł podac liczbę rund.
5. Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
6. Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’
'''
'''
kamien kamien 0 0
papier papier 0 0
nozyce nozyce 0 0   
kamien papier 0 1   
nozyce kamien 0 1
papier nozyce 0 1
'''
import random

number_of_rounds = int(input('Podaj liczbe rund: '))
n = 1
comp_wins = 0
user_wins = 0
dead_heat = 0
while n <= number_of_rounds:
    user_choice = input('Podaj jedna z figur: kamien/papier/nozyce ')
    comp_choice = random.choice(['kamien', 'papier', 'nozyce'])
    print(comp_choice)

    if user_choice.lower() == 'koniec':
        break
    if user_choice.lower() == comp_choice.lower():
        statement = 'Remis'
        dead_heat += 1
    elif (user_choice.lower() == 'papier' and comp_choice.lower() == 'nozyce') or \
            (user_choice.lower() == 'nozyce' and comp_choice.lower() == 'kamien') or \
            (user_choice.lower() == 'kamien' and comp_choice.lower() == 'papier'):
        statement = 'Komputer wygrywa!'
        comp_wins += 1
    else:
        statement = 'Uzytkownik wygrywa!'
        user_wins += 1

    n += 1

    # question = input('Chcesz grac dalej? y/n ')
    #
    # if question.lower() == 'y':
    #     continue
    # else:
    #     break

print(f'komputer/uzytkownik/remis: {comp_wins}/{user_wins}/{dead_heat}')

if comp_wins < user_wins:
    print('Wygrywa uzytkownik')
elif comp_wins > user_wins:
    print('Wygrywa komputer')
else:
    print('Remis')