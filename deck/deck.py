import array
import random
import string

DBShortCardNames = [ '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A' ];
DBShortSuitNames = [ 'c', 'd', 'h', 's' ];
DBLongSuitNames = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
DBLongCardNames = [ "Deuce", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace" ];
DECK_SIZE = 52
DBSingleNames = string.ascii_lowercase + string.ascii_uppercase

class Card:
    # constants for the card values.  to pack the values, the face values do not match the constants
    CV_ACE = 12
    CV_KING = 11
    CV_QUEEN = 10
    CV_JACK = 9
    CV_TEN = 8
    CV_NINE = 7
    CV_SIX = 4
    CV_FIVE = 3
    CV_FOUR = 2
    CV_THREE = 1
    CV_TWO = 0

    SV_CLUBS = 0
    SV_DIAMONDS = 1
    SV_HEARTS = 2
    SV_SPADES = 3

    def __init__(self, cardname):
        """ initialize a card either by index or by two character short name """
        if isinstance(cardname, str):
            if (len(cardname) == 1):
                self.set_card_by_single_name(cardname)
            else:
                self.set_card_by_short_name(cardname)
        elif isinstance(cardname, int):
            self.set_card_by_index(cardname)

    def is_valid(self):
        """ return if a card had a valid value """
        return ((self.value > -1) and (self.value < 13) and (self.suit > -1) and (self.suit < 4))  

    def get_index(self):
        """ get the canonical index for this card """
        return ((self.value * 4) + self.suit)
 
    def short_name(self):
        """ get a two character name for this card.  returns '??' if the card is invalid """
        if self.is_valid():
            return DBShortCardNames[self.value] + DBShortSuitNames[self.suit]
        else:
            return '??'

    def single_name(self):
        if self.is_valid():
            return DBSingleNames[self.get_index()]
        else:
            return '?'

    def set_card_by_single_name(self, name):
        return self.set_card_by_index(DBSingleNames.index(name))
        
    def long_name(self):
        if self.is_valid():
            return DBLongCardNames[self.value] + " of " + DBLongSuitNames[self.suit]
        else:
            return '??'

    def long_value(self):
        if self.is_valid():
            return DBLongCardNames[self.value]
        else:
            return '??'

    def set_card_by_index(self, index):
        """ set the card's value by canonical index"""
        self.value = (index / 4)
        self.suit = (index % 4)
        return self.is_valid()
    
    def set_value_by_name(self, valname):
        """ set the card's value by a short ('J') or long ('Jack') name"""
        if valname in DBShortCardNames:
            self.value = DBShortCardNames.index(valname)
        elif valname.capitalize() in DBLongCardNames:
            self.value = DBLongCardNames.index(valname.capitalize())
        else:
            return -1

    def set_suit_by_name(self, suitname):
        """ set the card's suit by a short ('h') or long ('Hearts') name"""
        if suitname in DBShortSuitNames:
            self.suit = DBShortSuitNames.index(suitname)
        elif suitname.capitalize() in DBLongSuitNames:
            self.suit = DBLongSuitNames.index(suitname.capitalize())
        else:
            return -1

    def set_card_by_short_name(self, cardname):
        """ set the card's value and suit by two character card name ('As' = 'Ace of spades')"""
        if len(cardname) != 2:
            return -1

        valname = cardname.upper()[0]
        suitname = cardname.lower()[1]

        if valname not in DBShortCardNames:
            return -1

        if suitname not in DBShortSuitNames:
            return -1

        self.value = DBShortCardNames.index(valname)
        self.suit = DBShortSuitNames.index(suitname)

class Deck:

    def __init__(self):
        self.pile = array.array('i', range(0, 52))
        
    def __len__(self):
        return len(self.pile)
        
    def shuffle(self):
        """ shuffle the deck in place """
        random.shuffle(self.pile)

    def reset(self):
        self.pile = array.array('i', range(0, 52))
        self.shuffle()

    def deal_one(self):
        """ pull the top card off the deck"""
        if len(self) == 0:
            return -1
        
        top_card = Card(self.pile.pop(0))
        return top_card

    def deal_hand(self, count):
        card_list = []
        for i in range(count):
            card_list.append(self.deal_one())
        return card_list

    def take_card(self, to_remove):
        """ remove a specific card from the deck"""
        index = to_remove.get_index()
        if index not in self.pile:
            return -1
        self.pile.remove(index)

    def sample_cards(self, to_sample):
        """ pull the top to_sample cards off the top of the deck, then replace """
        
        if (to_sample > len(self.pile)):
            return -1

        card_list = []
        for i in range(to_sample):
            card_list.append(Card(self.pile[i]))

        return card_list

    def deck_state(self):
        out = ''
        for i in self.pile:
            out = out + DBSingleNames[i]
        return out

    def restore_deck(self, new_state):
        self.pile = []
        for c in new_state:
            if c not in DBSingleNames:
                self.pile = []
                return -1
            else:
                new_card = DBSingleNames.index(c)
                if new_card in self.pile:
                    self.pile = []
                    return -1
                else :
                    self.pile.append(new_card)
        
        return True

        



    
