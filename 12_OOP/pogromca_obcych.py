import random

class Player:

    def blast(self, enemy):
        print('Gracz razi wroga.\n')
        shoot = random.randint(1, 11)
        if shoot >= 3:
            enemy.die()
        else:
            enemy.win()

class Alien:

    def die(self):
        print('Obcy z trudem łapie oddech, "To już koniec. Ale prawdziwie wielki koniec... \n',
              'Walczyliśmy do końca. Nie, to nie koniec. Larwy moje jednoczcie się! \n',
              'O tak one pomszczą mnie pewnego dnia... \n',
              'Żegnaj, okrutny Wszechświecie! Umieeeraaam"')

    def win(self):
        print('Obcy: "Mlah, mlah, mlah, smaczny ten gracz. Najdałem się, idę spać."')


if __name__ == '__main__':
    print('**********Śmierć Obcego**********')
    hero = Player()
    invader = Alien()
    hero.blast(invader)
    input('\n\nAby zakończyć program, naciśnij klawisz Enter.')