class PromptCopy(object):
    WELCOME = "Hello and welcome to a little card game called Shanghi"
    NUMBERS_ONLY = "Numbers only Chachi!"
    TRY_AGAIN = "Try again ya Goober."
    LETS_BEGIN = "Now that there are names to faces lets get some cards in hands."
    DEAL_READY = "Press any key to shuffle and toss."
    DISCARD_DEAD = "Discard is dead, gotta suck it up and buy from the deck."

    PLAYER = "Player"
    HAND = 'Hand'
    DOWN = 'Down'
    ROUND = 'Round'
    DISCARD_PILE = 'Discard Pile'

    PLAYER_COUNT = "Please input number of players 2-6 >>> "
    PLAYER_NAME = "Please enter a name for Player"
    PLAYER_NAME_CORRECT = "Is this name correct? Y/N"
    SEPARATOR = '♦♣♠♥=============♦♣♠♥\n'
    VSEPERATOR = '\n \n \n'

    PLAYER_CHOICES_DRAW = ", would you like to: \n1. Buy from the deck [1]\n2. Take discard [2]"
    PLAYER_CHOICES_PLACE = 'would you like to: \n1. Place Book [1]\n2. Place Run [2]\n'
    PLAYER_CHOICES_DISCARD = 'Discard!'
    PLAYER_DISCARD = "Discard please"

class DeckCopy(object):
    CARDWELLTITLE = "♦♣♠♥=====CARD WELL=====♦♣♠♥"
    CARDWELLDISCARD = "vvDISCARDvv"
    CARDWELLDECK = ">>DECK<<"
    CARDWELLDECKICON = "[=]"
    CADWELLDISPLAY = CARDWELLTITLE + '\n' + CARDWELLDISCARD + CARDWELLDECK + '\n'
