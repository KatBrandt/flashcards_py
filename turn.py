class Turn:
  def __init__(self, guess, card):
    self.guess = guess
    self.card = card

  def isCorrect(self):
    return self.guess == self.card.answer

  def feedback(self):
    if self.isCorrect():
      return "Correct!"
    else:
      return "Incorrect."