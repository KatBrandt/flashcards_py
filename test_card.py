import unittest
from card import Card

class TestCard(unittest.TestCase):

  def test_exists(self):
    question = "What is the capital of Alaska?"
    answer = "Juneau"
    category = "Geography"

    card_1 = Card(question, answer, category)
    self.assertIsInstance(card_1, Card, "Should be Card instance")

  def test_has_attributes(self):
    question = "What is the capital of Alaska?"
    answer = "Juneau"
    category = "Geography"

    card_1 = Card(question, answer, category)

    self.assertEqual(card_1.question, question)
    self.assertEqual(card_1.answer, answer)
    self.assertEqual(card_1.category, category)

if __name__ == '__main__':
  unittest.main()