from NoDak.services import PlayerServices, CardServices
from NoDak.constants import PromptCopy

class Game(object):
#ini player
#get shuffled deck
#deal cards
    def __init__(self):
        self.pc = PromptCopy()
        self.ps = PlayerServices()
        self.cs = CardServices()

    def start_game(self):
        print(self.pc.WELCOME)
        get_deck = self.cs.shuffled_deck()
        player_count = self.ps.player_count()
        player_dict = self.ps.player_setup(player_count=player_count)
        print(self.pc.LETS_BEGIN)
        input(self.pc.DEAL_READY)
        self.cs.deal_cards()

if __name__ == '__main__':
    game = Game()
    game.start_game()