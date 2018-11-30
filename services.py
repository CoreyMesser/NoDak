from random import randrange
from NoDak.models import Cards, Deck, Player, Session as session_store
from NoDak.constants import PromptCopy

class CardServices(object):
    def __init__(self):
        self.deck = Deck()

    def shuffle_check(self, num, shuffled_list, deck_size):
        while num in shuffled_list:
            num = randrange(0, deck_size)
        return num

    def shuffle(self, deck):
        shuffled_list = []
        deck_len = len(deck)
        for n in range(0, deck_len):
            r = randrange(0, deck_len)
            r = self.shuffle_check(num=r, shuffled_list=shuffled_list, deck_size=deck_len)
            shuffled_list.append(r)
        return shuffled_list

    def card_assigner(self, shuffled_list, deck):
        deck_len = len(deck)
        shuffled_deck = {}
        deck_index = 1
        for i in shuffled_list:
            shuffled_deck[i] = deck_index
            deck_index += 1
        return shuffled_deck

    def shuffled_deck(self):
        cards = Cards.cards
        sl = self.shuffle(deck=cards)
        ca = self.card_assigner(shuffled_list=sl, deck=cards)

        session_store.shuffle_list = sl
        session_store.deck_key = ca

        return sl, ca

    def deal_cards(self):
        num_players = session_store.player_count
        player_dict = session_store.player_dict
        shuffle_list = session_store.shuffle_list
        # round = session_store.round
        game_deck = self.deck.deck

        game_deck['remaining_cards'] = shuffle_list
        game_deck['deck_key'] = session_store.deck_key

        for player in player_dict:
            player_dict[player]['hand'] = game_deck['remaining_cards'][0]
            game_deck['remaining_cards'].pop(0)



        return

    def place_card(self, card):
        return

    def discard_card(self, card):
        return

    def take_card(self, pile, num):
        return

    def book_check(self, cards):
        return

    def run_check(self, cards):
        return

    def round_check(self):
        return


class PlayerServices(object):
    def __init__(self):
        self.cs = CardServices()
        self.pc = PromptCopy()
        self.pl = Player()

    def player_count(self):
        n = int(input(self.pc.PLAYER_COUNT))
        if n < 2 or n > 6:
            print(self.pc.TRY_AGAIN)
                # self.player_count()
        # except:
        #     print(self.pc.NUMBERS_ONLY)
        #     self.player_count()

        session_store.player_count = n
        return n

    def player_setup(self, player_count):
        players_dict = {}
        for n in range(0, player_count):
            name = input(self.pc.PLAYER_NAME)
            name = {name: self.pl.player}
            players_dict.update(name)

        session_store.player_dict = players_dict
        return players_dict




# cards dealt will be split into player dicts
# remaining cards will be left in a remaining_deck
# discard dict
# if reamining_cards == 0 than discard dict is shuffled back in

# if __name__ == '__main__':
#     cs = CardServices()
#     cs.shuffled_deck()



