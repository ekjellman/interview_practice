###
# Problem
###

# Return if a string is a permutation of a palindrome
# Example: "Tact Coa" -> True ("taco cat")

###
# Work
###

# Questions:
# Ignore spaces? (Assuming yes from example)
# Ignore case? (Assuming yes from example)
# Ignore non-letter characters? (Assuming yes from problem statement:
#   "A permutation is a rearrangement of letters")

import string
import collections

def is_palindrome_permutation(s):
  c = collections.Counter(s.lower())
  odd_counts = 0
  for letter in string.ascii_lowercase:
    if c[letter] % 2 != 0: odd_counts += 1
  return odd_counts <= 1

tests = [("Tact Coa", True),
         ("ABCabc", True),
         ("ABCDE", False),
         ("", True),
         ("ABCCBADE", False),
         ("ABCCBAD", True)]

for test in tests:
  s, expected = test
  print test, is_palindrome_permutation(s)

# Time: 8 minutes

###
# Mistakes / Bugs / Misses
###

# Line 26: Had > instead of <=
