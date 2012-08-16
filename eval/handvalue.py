import deck.deck

HandNameTemplates = [ 'unknown', "High Card", "Pair of {0}s", "{0}s and {1}s", "Trip {0}s", \
                          "{0} High Straight", "{0} High Flush", "{0}s Full of {1}s",\
                          "Quad {0}s", "{0} High Straight Flush" ]

class HandValue:
    HV_HIGH_CARD = 1
    HV_PAIR = 2
    HV_TWO_PAIR = 3
    HV_TRIPS = 4
    HV_STRAIGHT = 5
    HV_FLUSH = 6
    HV_FULL_HOUSE = 7
    HV_QUADS = 8
    HV_STR_FLUSH = 9

    """ represents the value of a hand in a few different ways.  The base method uses three values:
             type = an integer that represents the class of the hand (by the HV_ vals above)
             primary = the suit or value of the card that represents the value in the class
             secondary = the second value that represents the value of the hand
             tertiary = a bitmap of the values in the hand """

    def __init__(self, new_type, new_primary, new_secondary, new_tertiary):
        self.type = new_type
        self.primary = new_primary
        self.secondary = new_secondary
        self.tertiary = new_tertiary
        self.canonical = 0

    def get_canonical(self):
        """ return an integer that represents the value of a hand.  For all hands, if the canonical value is larger, then hand wins """
        
        # construct a 32 bit value, with the top three bits encoded as the hand type minus one
        # the primary is always in the range 0-12, so we reserve four bits for it
        # same with the secondary
        # the tertiary is a bitmap, needs at most 13 bits....these are the new LSB

        new_val = (self.type - 1) << 22
        new_val |= self.primary << 18
        new_val |= self.secondary << 14
        new_val |= self.tertiary

        return new_val

    def long_name(self):
        """ Print a string representation of the hand value """

        # slightly ugly hack here...the flush parameters are wonky, so we need to ignore the
        # secondary
        
        if (self.type != HV_FLUSH):
            return HandNameTemplates[self.type].format(deck.DBLongCardNames[self.primary],\
                                                           deck.DBLongCardNames[self.secondary])
        else:
            return HandNameTemplates[self.type].format(deck.DBLongCardNames[self.primary])

