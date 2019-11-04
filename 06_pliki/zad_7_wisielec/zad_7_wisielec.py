'''
7▹ Wisielec. Utwórz plik zawierający listę słów wg. kategorii np. zwierzęta, owoce etc. Poproś użytkownika
o podanie kategorii przed rozpoczęciemy gry. Następny wczytaj listę haseł do programu, wylosuj jedno
hasło z listy. Rozgrywka powinna być maksymalnie intuicyjna.
'''

import random

# with open('words.txt', 'r') as f:
#     lines = f.readlines()
# print(lines)
#
# for line in lines:
#     if lines[0] == 'f{category}'+':':
#         category = []
#
# print(category)

words = {'animals': ['owca', 'kon', 'wielblad', 'koza', 'krowa'],
         'fruits': ['jablko', 'gruszka', 'sliwka', 'ananas', 'mango'],
         'sport': ['pilka nozna', 'koszykowka', 'siatkowka', 'rower', 'plywanie'],
         'names': ['Sara', 'John', 'Sally', 'Ben', 'Alice', 'James']}
# jesli bylyby listy to jak to napisac? animals = [], fruits = []?


def menu():
    print('Welcome to hangmann game')
    print()
    category_name = False
    while not category_name:
        category = input('Please choose one of avaliable category of words: animals/friuts/sport/names ')
        if category not in words.keys():
            print('Please write correct name of category')
        else:
            category_name = True
    print(category)
    return category


def word_choice(category):
    chosen_word = random.choice(words[category])
    print('Wybor: ', chosen_word)
    return chosen_word


def hangman():
    # print('Category: ') jak tutaj wydrukowac kategorie?
    category_choice = menu()
    word = word_choice(category_choice)
    underscore_word = []
    for letter in word:
        underscore_word.append('_')
    try_to_guess = False
    game_round = 1
    while not try_to_guess:
        print('Word to gues: ', ' '.join(underscore_word))
        user_letter = input('Give me a letter, to quit write - exit ')
        if user_letter == 'exit':
            print(f'You lost, word to guess was: {word}, game round = {game_round}')
            try_to_guess = True
        elif user_letter == word:
            print(f'You win, You guess the word! It was {word}, game round = {game_round}')
            try_to_guess = True
        else:
            for position, letter in enumerate(word):
                if user_letter == letter:
                    underscore_word[position] = letter
            if ''.join(underscore_word) == word:
                print('Word to gues: ', ' '.join(underscore_word))
                print(f'You won, the word to guess was: {word}, game round = {game_round}')
                try_to_guess = True
        game_round += 1
    play_again()


def play_again():
    question = input('Do you want to play again? y/n ')
    if question.lower() == 'y':
        hangman()
    else:
        exit()



# comp_choice = random.choice(words[category_choice])
hangman()

# def main():
