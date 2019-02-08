###
# Problem
###

# Shuffle a deck of cards given a perfect random number generator.

###
# Work
###
# Questions:
# What kind of deck (assume you're just shuffling a list of objects)
# In-place? (Assume yes)

import random
def shuffle(my_list):
  for i in xrange(len(my_list)):
    swap_index = random.randint(i, len(my_list) - 1)
    my_list[i], my_list[swap_index] = my_list[swap_index], my_list[i]

# Tests
import collections
counts = collections.defaultdict(int)
for trial in xrange(1000000):
  cards = range(4)
  shuffle(cards)
  card_tuple = tuple(cards)
  counts[card_tuple] += 1
for card_tuple in counts:
  print card_tuple, counts[card_tuple]

# Time: 7 minutes

###
# Mistakes / Bugs / Misses
###
# Seems good
# TODO: Make a card about finding the min and max value in a hashtable
#       I would have liked to do that here
