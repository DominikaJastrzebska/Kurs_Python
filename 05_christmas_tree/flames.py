'''
Gra FLAMES
FLAMES to popularna gra, której nazwa postała od akronimu: Friends, Lovers, Affectionate, Marriage,
Enemies, Sibling. Choć gra nie pozwala dokładnie przewidzieć przyszłości to może sprawdzić się jako
andrzejkowa wróżba.
Jak znaleźć naszą parę?
1. Pobierz imion dwóch osób
2. Usuń wspólne litery występujące w obu imionach..
3. Policz pozostałe litery.
4. Użyj wyniku, by znaleźć prawdziwy związek między dwoma osobami.
Dokładne zasady gry FLAMES https://www.wikihow.com/Play-%22Flame%22
'''


def get_names():
    """
    function get names from woman and man
    :return: string which is the sum of names
    """
    woman_name = input('Put a woman name: ')
    man_name = input('Put a man name: ')
    names = woman_name + man_name
    return names.lower()


def leftover_letters(names):
    """
    function remove letters which the number of instance is more than one
    :param names: string
    :return: string with leftover letters
    """
    leftover_letters = ''
    for letter in names:
        counter = names.count(letter)
        # print(letter, counter)
        if counter == 1:
            leftover_letters += letter
        else:
            pass
    return leftover_letters


def count_leftover_letters(leftover_letters):
    """
    function get lenght of word
    :param leftover_letters: string
    :return: int - number of leftover letters
    """
    return len(leftover_letters)


if __name__ == '__main__':
    FLAMES = {1: 'Friends', 2: 'Lovers', 3: 'Affection', 4: 'Marriage', 0: 'Enemies'}
    names = get_names()
    leftover_letters = leftover_letters(names)
    number = count_leftover_letters(leftover_letters)

    print(FLAMES[number % 5])

# FLAMES = {1: 'Friends', 2: 'Lovers', 3: 'Affection', 4: 'Marriage', 0: 'Enemies'}
# print(FLAMES[1])
