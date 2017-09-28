import random

import config as cfg

class Deck:
    def __init__(self):
        self.cards = self.init_deck()
        self.remaining_cards = len(self.cards)

    def init_deck(self):
        cards = []
        for colour in range(cfg.NUM_COLOURS):
            for value in range(cfg.NUM_VALUES):
                for i in range(cfg.NUM_CARDS_PER_VALUE[value]):
                    cards.append((colour, value))
        random.shuffle(cards)
        return cards
        
    def draw_card(self):
        assert(self.remaining_cards > 0)
        self.remaining_cards -= 1
        return self.cards.pop()

    def remaining_cards(self):
        return self.remaining_cards
