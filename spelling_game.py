import random as rand
import json as json
#import datetime as dt

class SpellingGame:
  def __init__(self):
    # randomly select a word from filtered_words
    with open('main_word_common.json', 'r') as f:
      data = json.load(f)
    self.main_words = list(data.keys())
    self.word_of_day = self.main_words[rand.randint(0,
                                                    len(self.main_words) - 1)]
    #print(self.word_of_day)
    with open('filtered_words.json', 'r') as f:
      data2 = json.load(f)
    self.words = list(data2.keys())

    self.user_entry_words = []

  def main_word(self):
    return self.word_of_day

  def letters(self):
    return list(set(self.word_of_day))

  def check_valid(self, entry):
    if entry == self.word_of_day:
      return None
    if entry in self.words:
      if entry not in self.user_entry_words:
        self.user_entry_words.append(entry)
        return True
    return False

  def get_user_entry_words(self):
    return self.user_entry_words
