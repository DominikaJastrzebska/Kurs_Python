import random

names = ['Nubill', 'Alojra', 'Korgun', 'Polien', 'Karmeron', 'Korn']

chosen_name = random.choice(names)
print(chosen_name)
market_products = ['potatoes', 'tomatoes', 'strawberries', 'onion', 'garlic', 'raw fish']
forest_food = {'BB':'blueberries 🍒', 'B':'blackberries 🍇', 'M':'mushrooms 🍄'}
stolen_items = ['cat', 'dog', 'gold earrings', 'necklace', 'brush', 'cotton balls', 'clock', 'plate', 'lost kings crown', 'scizors']
quantity_stolen_item = {}
random_stolen_things = []

product = random.choice(market_products)
print(product)
quantity_food = random.randrange(1, 15)
quantity_days = random.randrange(1, 15)
print(quantity_days)
# forest_choice = input('What would You like to eat? blackberries - B, bluberries - BB, mashrooms - M ')


def init_game():
    place = input("Do You want to go to the forest - insert 'F' or to the town - insert 'T'? ")
    if place.lower() == 'f':
        forest_place()
    elif place.lower() == 't':
        town_place()


def death():
    print(f'{chosen_name} just died. Game over')
    try_again()


# def forest_choice_x():
#     forest_choice = input('What would You like to eat? blackberries - B, bluberries - BB, mashrooms - M ')
#     return forest_choice
        

def forest_place():
    answer = input(f'{chosen_name} are You hungry? Y/N ')
    if answer.lower() == 'y':
        forest_choice = input('What would You like to eat? blackberries - B, bluberries - BB, mashrooms - M ')
        print(f'Here You are some {forest_food[forest_choice.upper()]}, eat it.')
        if forest_choice.lower() == 'm':
            print(f'Unfortunately the {forest_food[forest_choice.upper()]} was poisonous.')
            death()
        else:
            wizzard(forest_food[forest_choice.upper()], wizard_name='Alindur', location=' Wilderness')
    else:
        print('Maybe next time, You know, where to find me.')


def wizzard(food, wizard_name, location):
    sentence = f"{chosen_name} met a {wizard_name.capitalize()}, the great wizzard who showed on his path in {location}"
    print(sentence)
    print('The wizard told a story about a very gravy dragon, who is stealing treasures from people for years.'
          'Whoever gets to kill the beast, will become the richest man on land')
    kill_dragon = input(f'Does {chosen_name} want to kill the dragon? Y/N ')
    if kill_dragon.lower() == 'y':
        print('You lost. The dragon is stronger')
        death()
    else:
        print(f'The {chosen_name} lived happily ever after and for rest of his life eat {food}')


def town_place():
    print(f'{chosen_name} went to the market place and got {quantity_food} {product}')
    print(f'This will be his food for the next {quantity_days} days')
    if quantity_days >= 7:
        print(f"{chosen_name} should walk for 2 days to the forrest in search sth to eat, "
              f"because this isn't enough food to survive")
        forest_place()
    else:
        print(f'{chosen_name} has to steel something. ')
        quantity_of_houses = int(input('Decide, how many houses do you wand to rub: '))
        i = 0
        while i <= quantity_of_houses:
            stolen_thing = random.choice(stolen_items)
            random_stolen_things.append(stolen_thing)
            i += 1
        for stolen_thing in random_stolen_things:
            if stolen_thing in quantity_stolen_item:
                quantity_stolen_item[stolen_thing] += 1
            else:
                quantity_stolen_item[stolen_thing] = 1
        print(f'{chosen_name} has stolen: ')
        for keys, values in quantity_stolen_item.items():
            print(values, keys, end=', ')


def try_again():
    again = input('Chcesz zagrac jeszcze raz? ')
    if again.lower() == 'y':
        init_game()
    else:
        print('May we meet again.')
        exit()


init_game()
print('lala')
