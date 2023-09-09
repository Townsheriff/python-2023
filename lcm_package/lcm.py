class LetterCounter:
  def __init__(self, text):
    self.text = text
  
  def count_same_letters(self, letter):
    return len(self.text) - len(self.text.replace(letter, ""))