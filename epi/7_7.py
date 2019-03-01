###
# Problem
###

# Given a phone number, return all the possible character sequences that
# correspond to the phone number. They don't have to be valid words.

###
# Work
###
# Length of the phone number?
# Input? (assume string)
# How to handle 0 and 1? (Assume the number won't have them)

# Cheeky answer:
import itertools

def phone_chars(s, letter_map):
  # TODO: error checking?  0 and 1
  char_list = [letter_map[x] for x in s]
  for p in itertools.product(*char_list):
    yield "".join(p)

# Test:
letter_map = {"2": "ABC", "3": "DEF", "4": "GHI", "5": "JKL", "6": "MNO",
              "7": "PQRS", "8": "TUV", "9": "WXYZ"}
for p in phone_chars("2276696", letter_map):
  print p

# Less cheeky answer
def phone_chars(s, letter_map):
  if len(s) == 0:
    yield ""
    raise StopIteration
  for letter in letter_map[s[0]]:
    for answer in phone_chars(s[1:], letter_map):
      yield letter + answer

letter_map = {"2": "ABC", "3": "DEF", "4": "GHI", "5": "JKL", "6": "MNO",
              "7": "PQRS", "8": "TUV", "9": "WXYZ"}
for p in phone_chars("2276696", letter_map):
  print p

# Time:

###
# Mistakes / Bugs / Misses
###
# Screwed up the letter map (put , instead of : a couple times)
# Forgot how itertools.product worked. Each list is an argument, so you need *.
# (TODO: Make card)
# In less cheeky answer:
# Forgot to raise StopIteration (TODO: make card. Need it because otherwise it
#   continues past base case and we get an IndexError
# yielded s[0] + answer instead of letter + answer at 37
