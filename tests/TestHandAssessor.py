import unittest
from cards.HandAssessor import HandAssessor

class TestHandAssessor(unittest.TestCase):
    def setUp(self):
        self.hand = HandAssessor()



    def testCardsAreValidated(self):
        test_cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        test_suits = ['D', 'C', 'H', 'S']
        for test_card in test_cards:
            for test_suit in test_suits:
                self.assertEquals(self.hand.validate_card( test_card + test_suit), True, test_card + test_suit +  " is a valid card")

    def testInvalidCardsAreRejected(self):
        self.assertEquals(self.hand.validate_card('0C'),False, 'invalid card number')
        self.assertEquals(self.hand.validate_card('2A'),False, 'invalid suit')
        self.assertEquals(self.hand.validate_card('1B'),False, 'invalid card number and suit')

    def testHeartsIdentified(self):
        self.assertEquals(self.hand.isHeart('AH'),True, "Heart returns True")
        self.assertEquals(self.hand.isHeart('AC'),False, "Club returns False")
        self.assertEquals(self.hand.isHeart('AS'),False, "Spade returns False")
        self.assertEquals(self.hand.isHeart('AD'),False, "Diamond returns False")

    def testDiamondsIdentified(self):
        self.assertEquals(self.hand.isDiamond('AH'),False, "Heart returns False")
        self.assertEquals(self.hand.isDiamond('AC'),False, "Club returns False")
        self.assertEquals(self.hand.isDiamond('AS'),False, "Spade returns False")
        self.assertEquals(self.hand.isDiamond('AD'),True, "Diamond returns True")

    def testClubIdentified(self):
        self.assertEquals(self.hand.isClub('AH'),False, "Heart returns False")
        self.assertEquals(self.hand.isClub('AC'),True, "Club returns False")
        self.assertEquals(self.hand.isClub('AS'),False, "Spade returns False")
        self.assertEquals(self.hand.isClub('AD'),False, "Diamond returns True")

    def testSpadesIdentified(self):
        self.assertEquals(self.hand.isSpade('AH'),False, "Heart returns False")
        self.assertEquals(self.hand.isSpade('AC'),False, "Club returns False")
        self.assertEquals(self.hand.isSpade('AS'),True, "Spade returns True")
        self.assertEquals(self.hand.isSpade('AD'),False, "Diamond returns False")
