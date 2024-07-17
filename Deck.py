import Card
import random
class Deck:

    def __init__(self, cards : list):
        self.cards = cards
        self.top = 51

    def pop_card(self) -> Card:
        last = self.cards[self.top]
        self.top -= 1
        return last
    
    def shuffle_cards(self):
        for i in range(52):
            j = random.randint(0, i)
            temp = self.cards[i]
            self.cards[i] = self.cards[j]
            self.cards[j] = temp


