class Cards(object):
    card_suit = ['♥', '♦', '♣', '♠']
    card_ranks_num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_ranks_face = ['10', 'J', 'Q', 'K', 'A']
    card_ranks_sp = ['Jk']
    card_values = [0, 5, 10, 25, 50]

    card_model = {'card': {'suit': '', 'rank': ''},
                  'value': 0}

    card_model = {'card_face':}

    cards = {0: ["#", 0],
             1: ["2♥", 5],
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
            'last_discard': {'card': 0,
                             'player': ''},
            'discard_pile': [],
            'master_key': {},
            'num_decks': 3}

class Rounds(object):
    rounds = {1: ['1 Book', 10],
              2: ['1 Run', 10],
              3: ['2 Runs', 10],
              4: ['3 Books', 10],
              5: ['2 Books 1 Run', 12],
              6: ['2 Runs 1 Book', 12],
              7: ['2 Books 2 Runs', 12],
              8: ['3 Runs', 12]}

class Session(object):
        player_count = 0
        player_dict = {}
        game_round = {'round': 1,
                      'stage': []}
        game_deck = {}
        turns = {'turns_list': [],
                 'current_turn': [],
                 'previous_turn': [],
                 'stage': 1}

# ♦♣♠♥