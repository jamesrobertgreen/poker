class HandAssessor():
    valid_cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    valid_suits = ['D','C','H','S']

    def __init__(self):
        pass

    def validate_card(self,card):
        # Valid if it is 1-A and a valid suit
        if card[0] in self.valid_cards and card[1] in self.valid_suits:
            return True
        else:
            return False

    def identify_hand(self,hole_cards,river):

        return ''

    def isHeart(self,card):
        if(card[1] == 'H'):
            return True
        else:
            return False

    def isDiamond(self,card):
        if(card[1] == 'D'):
            return True
        else:
            return False

    def isClub(self,card):
        if(card[1] == 'C'):
            return True
        else:
            return False

    def isSpade(self, card):
        if (card[1] == 'S'):
            return True
        else:
            return False

