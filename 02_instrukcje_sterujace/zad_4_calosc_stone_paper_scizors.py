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

while True:
    user_choice = input('Podaj jedna z figur: kamien/papier/nozyce ')
    comp_choice = random.choice(['kamien', 'papier', 'nozyce'])
    print('Komputer:', comp_choice)

    if user_choice.lower() == comp_choice.lower():
        print('Remis')
    elif (user_choice.lower() == 'papier' and comp_choice.lower() == 'nozyce') or \
            (user_choice.lower() == 'nozyce' and comp_choice.lower() == 'kamien') or \
            (user_choice.lower() == 'kamien' and comp_choice.lower() == 'papier'):
        print('Komputer wygrywa!')
    else:
        print('Uzytkownik wygrywa!')

    question = input('Chcesz grac dalej? y/n ')

    if question.lower() == 'y':
        continue
    else:
        break
