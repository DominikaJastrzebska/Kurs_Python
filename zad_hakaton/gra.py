import random

names = ['Nubill', 'Alojra', 'Korgun', 'Polien', 'Karmeron', 'Korn']

chosen_name = random.choice(names)
print(chosen_name)
market_products = ['potatoes', 'tomatoes', 'strawberries', 'onion', 'garlic', 'raw fish']
forest_food = {'BB':'blueberries 🍒', 'B':'blackberries 🍇', 'M':'mushrooms 🍄'}

place = input("Do You want to go to the forest - insert 'F' or to the town - insert 'T'? ")
product = random.choice(market_products)
print(product)
quantity_food = random.randrange(1, 15)
quantity_days = random.randrange(1, 15)
print(quantity_days)

# def death():
#     while True:
        


def forest_place():
    answer = input(f'{chosen_name} are You hungry? Y/N ')
    if answer.lower() == 'y':
        forest_choice = input('What would You like to eat? blackberries - B, bluberries - BB, mashrooms - M')
        print(f'Here You are some {forest_food[forest_choice]}, eat it.')
        if forest_choice.lower() == 'm':
            print(f'Unfortunatelly the {forest_food[forest_choice]} was poisonous.')
            death()
            
    else:
        print('Maybe next time, You know, where to find me.')


def town_place():
    print(f'{chosen_name} went to the market place and got {quantity_food} {product}')
    print(f'This will be his food for the next {quantity_days} days')
    if quantity_days >= 4:
        print(f"{chosen_name} should walk for 2 days to the forrest in search sth to eat, "
              f"because this isn't enough food to survive")
        forest_place()
    else:
        print('You have to steel something.')


if place.lower() == 'f':
    forest_place()
elif place.lower() == 't':
    town_place()

def try_again():
    again = input('Chcesz zagrac jeszcze raz? ')
    if again.lower() == 'y':
        guess_game()
    else:
        exit()