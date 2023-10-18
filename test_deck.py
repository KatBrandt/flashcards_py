import unittest
from card import Card
from turn import Turn
from deck import Deck

class TestCard(unittest.TestCase):
  def setUp(self):
    self.card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    self.card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    self.card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    self.cards = [self.card_1, self.card_2, self.card_3]


  def test_it_exists(self):
    deck = Deck(self.cards)

    self.assertIsInstance(deck, Deck)

if __name__ == '__main__':
  unittest.main()
