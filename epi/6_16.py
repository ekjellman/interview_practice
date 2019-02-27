###
# Problem
###

# Given a list of n numbers, their probabilities which sum up to 1, and a random
# number generator that produces values from [0, 1], how would you generate one
# of the n numbers according to the specified probabilities?

###
# Work
###
# Questions:
# Can I modify the list of probabilities? (if not I'll use O(n) space)
# (Assuming no) (If not, I'd modify probs in place)
# Size of n (binary search vs linear search in terms of code complexity

import random

class RNG(object):
  def __init__(self, numbers, probs):
    assert len(numbers) == len(probs)
    assert len(numbers) >= 1
    assert sum(probs) == 1.0  # Or possibly get it close for float issues
    self.numbers = numbers
    self.probs = probs[:]
    for i in xrange(1, len(numbers)):
      self.probs[i] = self.probs[i] + self.probs[i-1]

  def next_number(self):
    index = self.get_index(random.random())
    return self.numbers[index]

  def get_index(self, x):
    # Test this thing
    low = 0
    high = len(self.probs) - 1
    while low < high:
      mid = (low + high) / 2
      if self.probs[mid] < x:
        low = mid + 1
      elif self.probs[mid] > x:
        high = mid
      else:
        return mid
    return high

# Test
import collections
numbers = [0, 1, 2, 3, 4]
probs = [.0, .1, .2, .3, .4]
counts = collections.defaultdict(int)
rng = RNG(numbers, probs)
for i in xrange(10000):
  counts[rng.next_number()] += 1
print counts

numbers = [3, 5, 7, 11]
probs = [9/18.0, 6/18.0, 2/18.0, 1/18.0]
counts = collections.defaultdict(int)
rng = RNG(numbers, probs)
for i in xrange(10000):
  counts[rng.next_number()] += 1
print counts

# Time:

###
# Mistakes / Bugs / Misses
###
# forgot -1 in line 36
# Forgot self in lines 39 and 41
