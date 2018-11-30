from random import randrange
from nodak.models import Cards

class CardServices(object):

    def shuffle_check(self, num, shuffled_list, deck_size):
        while num in shuffled_list:
            num = randrange(1, deck_size)
        return num

    def shuffle(self, deck):
        shuffled_list = []
        deck_len = len(deck)
        for n in range(1, deck_len+1):
            r = randrange(1, deck_len)
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

    def deal_cards(self):
        cards = Cards.cards
        sl = self.shuffle(deck=cards)
        ca = self.card_assigner(shuffled_list=sl, deck=cards)
        return ca

    # cards dealt will be split into player dicts
# remaining cards will be left in a remaining_deck
# discard dict
# if reamining_cards == 0 than discard dict is shuffled back in

if __name__ == '__main__':
    cs = CardServices()
    cs.deal_cards()




