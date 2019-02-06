###
# Problem
###

# Given a list of valid words and a sequence of digits, write a function to
# return the words that match those digits on an old cell phone.

# Ex: 8733 -> tree, used   (8 -> tuv, 7 -> pqrs, 3 -> def)

###
# Work
###
# Questions: Are we going to call this function a lot? If so, caching or (more
#            likely) precomputing all the words into a hashtable (assume yes)
#            Case? (We'll convert to upper)
#            Punctuation / etc? (Assume all a-z)

import collections

class WordFinder(object):
  def __init__(self, word_list):
    self.table = self.make_table(word_list) 

  def make_table(self, words):
             #abcdefghijklmnopqrstuvwxyz
    values = "22233344455566677778889999"
    table = collections.defaultdict(list)
    for word in words:
      letter_numbers = []
      for letter in word.upper():
        letter_numbers.append(values[ord(letter) - ord("A")])
      table[int("".join(letter_numbers))].append(word)
    return table

  def lookup(self, digits):
    return self.table[digits]

# Test:
with open("/usr/share/dict/words", "r") as file_in:
  words = file_in.readlines()
  words = [word.strip() for word in words]

wf = WordFinder(words)
print wf.lookup(8733)

# Time: 11 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't really consider the slower solutions. :shrug:
