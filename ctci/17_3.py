###
# Problem
###

# Write a method to randomly generate a set of m integers from a list of size
# n. Each element must have an equal probability of being chosen.

###
# Work
###
# Questions:
# Sizes of m and n? (assume fits in memory)
# Invalid inputs? (Assume input is valid)
#   -- negative m, m > n, etc.

import random

def random_set(numbers, m):
  assert m >= 0 and m <= len(numbers)
  numbers_copy = numbers[:]
  random.shuffle(numbers_copy)
  return numbers_copy[:m]   # or turn into a set, or whatever.

# Alternate strategies:
# -- Make copy, pick items one at a time.
# -- Pick indices one at a time, using a set to ensure no duplicates, until you
#    have m
# -- Shuffle the original list then return the slice the same way, if you can
#    modify numbers

# Time: 5 minutes

###
# Mistakes / Bugs / Misses
###
