from random import randrange
from app.models import Cards, Deck, Player, Session, Rounds
from app.constants import PromptCopy

class CardServices(Cards, Deck):
    def __init__(self):
        pass

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
        return sl, ca

    def deal_cards(self, session):
        player_dict = session.player_dict
        game_deck = session.game_deck
        game_round = session.game_round[1]

        while game_round > 0:
            for player in player_dict:
                hand = player_dict[player]['hand']
                hand.append(game_deck['remaining_cards'][0])
                game_deck['remaining_cards'].pop(0)
            game_round -= 1
        return session

    def get_game_deck(self, shuffle_list, deck_key):
        game_deck = Deck().deck
        game_deck['remaining_cards'] = shuffle_list
        game_deck['deck_key'] = deck_key
        return game_deck

    def display_cards(self, player, session):
        player_dict = session.player_dict
        hand_list = []
        placed_list = []
        #check for placed cards player_dict[player][down]
        for card in player_dict[player]['hand']:
            hand_list.append(self.card_translator(session=session, card=card))

        for placed in player_dict[player]['down']:
            placed_list.append(self.card_translator(session=session, card=placed))

        return hand_list, placed_list

    def card_translator(self, session, card):
        card_key = session.game_deck['deck_key'][card]
        return Cards().cards[card_key][0]

    def place_card(self, card):
        return

    def discard_card(self, session):
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
        return n

    def player_setup(self, player_count):
        players_dict = {}
        for n in range(0, player_count):
            name = input(self.pc.PLAYER_NAME + '{} >>> '.format(n+1))
            player = {name: {'hand': [],
                            'down': [],
                            'score': 0}}
            players_dict.update(player)
        return players_dict


class GameServices(object):
    session = Session()

    def __init__(self):
        self.cs = CardServices()
        self.pc = PromptCopy()

    def session_store(self, player_count, player_dict, game_round, game_deck):
        self.session.player_count = player_count
        self.session.player_dict = player_dict
        self.session.game_round = game_round
        self.session.game_deck = game_deck
        return self.session

    def get_round(self, current_round):
        game_rounds = Rounds()
        return game_rounds.rounds[current_round]

    def display_table(self, session):
        player_dict = session.player_dict
        discard_pile = self.cs.discard_card(session=session)

        print(self.pc.ROUND + ':: {}'.format(session.game_round))
        print(self.pc.DISCARD_PILE + ':: {}'.format(session.game_deck['discard_pile']))
        print(self.pc.SEPARATOR)

        for player in player_dict:
            print(self.pc.PLAYER + ':: {}'.format(player))
            hand, down = self.cs.display_cards(session=session, player=player)
            print(self.pc.HAND + ':: {}'.format(hand))
            print(self.pc.DOWN + ':: {}'.format(down))
            print(self.pc.SEPARATOR)

    def get_turn(self, session, player):
        # ask if player would like to buy discard
        # check discard
            # once a discard is dead it is returned to the remaining cards
        # if player does not want discard a card is added to their hand from the top of the deck
        # ask if player would like to report pairings
        # allow the player to input pairing
        # check player input
        # TRUE remove cards from hand and place in down
        # FALSE go to ask
        # IF/WHEN ask == no
        #
        # ask player which card they would like to discard


        return





# cards dealt will be split into player dicts
# remaining cards will be left in a remaining_deck
# discard dict
# if reamining_cards == 0 than discard dict is shuffled back in

# if __name__ == '__main__':
#     cs = CardServices()
#     cs.shuffled_deck()




