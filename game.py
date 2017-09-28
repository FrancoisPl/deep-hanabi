import config as cfg
from deck import Deck
from player import Player

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        for player in range(cfg.NUM_PLAYERS):
            player_cards = [self.deck.draw_card() for card_number in range(cfg.NUM_CARDS_PER_HAND)]
            self.players.append(Player(player_cards))
                
    
if __name__=='__main__':
    game = Game()
    import pdb
    pdb.set_trace()