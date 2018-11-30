class Cards(object):
    cards = {1: ["2♥", 5],
             2: ["3♥", 5],
             3: ["4♥", 5],
             4: ["5♥", 5],
             5: ["6♥", 5],
             6: ["7♥", 5],
             7: ["8♥", 5],
             8: ["9♥", 5],
             9: ["10♥", 10],
             10: ["J♥", 10],
             11: ["Q♥", 10],
             12: ["K♥", 10],
             13: ["A♥", 25],
             14: ["2♦", 5],
             15: ["3♦", 5],
             16: ["4♦", 5],
             17: ["5♦", 5],
             18: ["6♦", 5],
             19: ["7♦", 5],
             20: ["8♦", 5],
             21: ["9♦", 5],
             22: ["10♦", 10],
             23: ["J♦", 10],
             24: ["Q♦", 10],
             25: ["K♦", 10],
             26: ["A♦", 25],
             27: ["2♣", 5],
             28: ["3♣", 5],
             29: ["4♣", 5],
             30: ["5♣", 5],
             31: ["6♣", 5],
             32: ["7♣", 5],
             33: ["8♣", 5],
             34: ["9♣", 5],
             35: ["10♣", 10],
             36: ["J♣", 10],
             37: ["Q♣", 10],
             38: ["K♣", 10],
             39: ["A♣", 25],
             40: ["2♠", 5],
             41: ["3♠", 5],
             42: ["4♠", 5],
             43: ["5♠", 5],
             44: ["6♠", 5],
             45: ["7♠", 5],
             46: ["8♠", 5],
             47: ["9♠", 5],
             48: ["10♠", 10],
             49: ["J♠", 10],
             50: ["Q♠", 10],
             51: ["K♠", 10],
             52: ["A♠", 25],
             53: ["Jk", 50],
             54: ["Jk", 50]}

class Player(object):
    player = {'hand': [],
              'down': [],
              'score': 0}

class Deck(object):
    deck = {'remaining_cards': [],
            'discard_pile': [],
            'master_key': {}}

class Rounds(object):
    rounds = {1: '1 Book',
              2: '1 Run',
              3: '2 Runs',
              4: '3 Books',
              5: '2 Books 1 Run',
              6: '2 Runs 1 Book',
              7: '2 Books 2 Runs',
              8: '3 Runs'}

class Session(object):
    def __init__(self):
        self.player_count = 0
        self.player_dict = {}
        self.round = 1
        self.deck_key = {}
        self.shuffle_list = []
        self.deck = {}

    def session_store(self, player_count, player_dict, round, deck_key, shuffle_list):
        self.player_count = player_count
        self.player_dict = player_dict
        self.round = round
        self.deck_key = deck_key
        self.shuffle_list = shuffle_list

    def get_session(self):
        return

# ♦♣♠♥