###
# Problem
###

# Design an algorithm that creates uniformly random permutations of
# [0, 1, ..., n-1]. You are given a random number generator that returns
# integers in the set [0, 1, ... n-1] with equal probability. Use as few calls
# to it as possible.

###
# Work
###
# Questions:
# code complexity / calls to rng tradeoffs
# size of n

# Approaches:
# Use a standard shuffling routine. This probably uses about n calls to the
# generator. For the first few numbers we could figure get about one item per
# call with some waste, and then later when there are fewer items left we could
# get a few items with one call. This would be complex.
# Another approach would be to calculate a number from 0 to n! using logn n!
# calls to the generator. This should be better, although occasionally we'll
# have to redo it.

# I'm going to try to code this approach.

import random
import math
class RNG(object):
  def __init__(self, n):
    self.n = n

  def next_number(self):
    return random.randint(0, self.n-1)

def random_permutation(n):
  # Not worrying about the algorithmic complexity of removing items from lists.
  # There are optimizations here, just trying to minimize calls to RNG
  perm_num = generate_perm_number(n)
  items = range(n)
  result = []
  while items:
    group_size = math.factorial(len(items) - 1)
    next_index = perm_num / group_size
    perm_num = perm_num % group_size
    result.append(items.pop(next_index))
  return result

def generate_perm_number(n):
  rng = RNG(n)
  max_perm_num = math.factorial(n) - 1
  while True:
    total = 0
    factor = 1
    while factor < max_perm_num:
      total += factor * rng.next_number()
      factor *= n
    if total <= max_perm_num:
      return total

# Test:
import collections
counts = collections.defaultdict(int)
for i in xrange(10000):
  p = tuple(random_permutation(5))
  counts[p] += 1
for p in counts:
  print p, counts[p]
print len(counts)

# Time: 20 minutes

###
# Mistakes / Bugs / Misses
###
# had n instead of self.n at 35
# had remove instead of pop at 47
# Had 5 instead of n at line 58
# I guess I should have asked questions about how that random number generator
# actually worked. Apparently we can use it to get numbers from m to n.
# Mine still makes less calls though. ;-)
