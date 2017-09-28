import random

import config as cfg

class Deck:
    def __init__(self):
        self.cards = self.init_deck()

    def init_deck(self):
        cards = []
        for colour in range(cfg.NUM_COLOURS):
            for value in range(cfg.NUM_VALUES):
                for i in range(cfg.NUM_CARDS_PER_VALUE[value]):
                    cards.append((colour, value))
        random.shuffle(cards)
        return cards
        
    def draw_card():
        return
    
if __name__=='__main__':
    deck = Deck()
    import pdb
    pdb.set_trace()
    