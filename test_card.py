import unittest

from card import Card

class TestCard(unittest.TestCase):

  def test_exists(self):
    question = "What is the capital of Alaska?"
    answer = "Juneau"
    category = "Geography"

    card_1 = Card(question, answer, category)
    self.assertIsInstance(card_1, Card, "Should be Card instance")


if __name__ == '__main__':
  unittest.main()