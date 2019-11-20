import random


class Orchid:
    kingdom = 'Plants'

    def __init__(self, color, species, flowering_season):
        self.color = color
        self.species = species
        self.flowering_season = flowering_season

    def blossom(self):
        flakes = ['🌾', '💐', '🌷', '🌹']
        return random.randint(2, 10) * random.choice(flakes)

    def throw_flowers(self):
        flowers = ['🌺', '🌸', '🥀']
        return random.randint(1, 3) * random.choice(flowers)


obj_orchid_white = Orchid('white', 'Pallens', 'spring')
obj_orchid_purple = Orchid('purple', 'Mascula', 'all year')

print(obj_orchid_white.flowering_season)
print(obj_orchid_white.blossom())
print(obj_orchid_white.throw_flowers())
print(obj_orchid_purple.blossom())
print(obj_orchid_purple.throw_flowers())
