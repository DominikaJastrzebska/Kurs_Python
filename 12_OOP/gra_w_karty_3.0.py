class Card(object):
    """Karta do gry"""
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['♣', '♦', '♥', '♠']  # c - Clubs(Trefl), d - Diamond(Karo), h - Hearts(Kier), s - Spades(Pik), ♣ - trefl, ♦ - karo, ♥ - kier, ♠ - pik

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class UnprintableCard(Card):
    """Karta, której ranga i kolor nie są ujawnione przy jej wyświetlaniu."""
    def __str__(self):
        return '<utajniona>'


class PositionableCard(Card):
    """Karta, która może być odkryta lub zakryta."""
    def __init__(self, rank, suit, face_up=True):
        super().__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super().__str__()
        else:
            rep = 'XX'
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


card1 = Card('A', '♣')
card2 = UnprintableCard('A', '♦')
card3 = PositionableCard('A', '♥')

print('Wyświetlanie obiektu klasy Card:')
print(card1)
print('Wyświetlanie obiektu klasy UnprintableCard:')
print(card2)
print('Wyświetlanie obiektu klasy PositionableCard:')
print(card3)
print('Odwrócenie stanu obiektu klasy PositionableCard (odkrycie - zakrycie karty).')
card3.flip()
print('Wyświetlenie obiektu klasy PositionableCard:')
print(card3)
input('\n\nAby zakończyć program, naciśnij Enter.')



