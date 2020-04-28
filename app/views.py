from services import PlayerServices, CardServices, GameServices
from constants import PromptCopy
from flask import Flask, render_template

app = create_app()

@app.route('/')
def home():
    return '__Shanghai Bitches__'

class Game(object):
#ini player
#get shuffled deck
#deal cards
    def __init__(self):
        self.pc = PromptCopy()
        self.ps = PlayerServices()
        self.cs = CardServices()
        self.gs = GameServices()

    def start_game(self):
        print(self.pc.WELCOME)
        game_round = self.gs.get_round(current_round=1)
        shuffle_list, deck_key = self.cs.shuffled_deck()
        game_deck = self.cs.get_game_deck(shuffle_list=shuffle_list, deck_key=deck_key)
        player_count = self.ps.player_count()
        player_dict = self.ps.player_setup(player_count=player_count)
        session = self.gs.session_store(player_count=player_count,
                                        player_dict=player_dict,
                                        game_round=game_round,
                                        game_deck=game_deck)
        print(self.pc.LETS_BEGIN)
        input(self.pc.DEAL_READY)
        self.cs.deal_cards(session=session)
        self.gs.display_table(session=session)

#
# if __name__ == '__main__':
#     game = Game()
#     game.start_game()
