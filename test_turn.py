import unittest
from card import Card
from turn import Turn

class TestCard(unittest.TestCase):
  def test_it_exists(self):
    question = "What is the capital of Alaska?"
    answer = "Juneau"
    category = "Geography"
    card_1 = Card(question, answer, category)
    turn_1 = Turn("Denver", card_1)

    self.assertIsInstance(turn_1, Turn)

  def test_it_checks_guess(self):
    question = "What is the capital of Alaska?"
    answer = "Juneau"
    category = "Geography"
    card_1 = Card(question, answer, category)
    turn_1 = Turn("Denver", card_1)
    turn_2 = Turn("Juneau", card_1)

    self.assertFalse(turn_1.isCorrect())
    self.assertTrue(turn_2.isCorrect())

  def test_it_returns_feedback(self):
    question = "What is the capital of Alaska?"
    answer = "Juneau"
    category = "Geography"
    card_1 = Card(question, answer, category)
    turn_1 = Turn("Denver", card_1)
    turn_2 = Turn("Juneau", card_1)

    self.assertEqual(turn_1.feedback(), "Incorrect.")
    self.assertEqual(turn_2.feedback(), "Correct!")


if __name__ == '__main__':
  unittest.main()