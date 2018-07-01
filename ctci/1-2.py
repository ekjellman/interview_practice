###
# Problem
###

# Given two strings, write a method to decide if one is a permutation of the
# other

###
# Work
###

# Questions:
# -- Length of string (Assume unknown)
# -- Does case matter (Assume yes)
# -- Does space / punctuation matter? (Assume yes)
# -- What kinds of characters? (Assume ASCII)

import collections

def is_permutation(a, b):
  return collections.Counter(a) == collections.Counter(b)

tests = [("abc", "bca", True),
         ("abc", "dca", False),
         ("Space Test", "Test Space", True),
         ("Space Test", "TestSpace", False),
         ("Case Test", "case test", False),
         ("case test", "test case", True),
         ("aaaa", "aaaaa", False)]

for test in tests:
  a, b, expected = test
  print test, expected, is_permutation(a, b)

# Time: 6 minutes

###
# Mistakes / Bugs / Misses
###

# Did not add check for lengths of strings (if two strings are different
#   lengths, we know they're not permutations of each other)
# Did not consider worse / other approaches (i.e. Sorting the string)
