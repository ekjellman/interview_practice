###
# Problem
###

# How would you compute the parity of a very large number of 64-bit words?

###
# Work
###
# Questions:
# How many is very large? Millions? Thousands? Billions? (Assume billions)
#   -- Basically: Is precomputation worth the hassle?
# Do we know the words are all 64-bit? (Assume yes)
#   -- Extensibility, etc
# Output type? (0 or 1? True or False?) (Assume 0/1)

class ParityCalc(object):
  def __init__(self):
    self.cache = self.make_cache()

  def make_cache(self):
    # Alternately: Use n & n-1 trick, but this is faster in python
    cache = []
    for i in xrange(65536):
      cache.append(bin(i).count("1") % 2)
    return cache

  def compute_parity(self, n):
    n_32 = ((n & 0xFFFFFFFF00000000) >> 32) ^ (n & 0xFFFFFFFF)
    n_16 = ((n_32 & 0xFFFF0000) >> 16) ^ (n_32 & 0xFFFF)
    return self.cache[n_16]

# Tests:
import random
pc = ParityCalc()
for i in xrange(100):
  n = random.randint(0, 2**64-1)
  expected = bin(n).count("1") % 2
  actual = pc.compute_parity(n)
  print actual == expected, actual, expected, n

# Other approaches:
# Use gmpy2 (probably what I'd actually do)
# Use another language and pop_count
# Really, we'd have to do some extensive testing on what the best approach is
# if we're using Python. The way numbers and binary are dealt with in Python
# makes me really unsure if this is fastest.
# Particularly, the timing of looking up something in the cache vs. recomputing
# it, particularly with gmpy2 or another language's pop_count
# Hopefully though, this shows some techniques.

# Time: 20 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot to have make_cache create the cache
# in line 30, had n instead of n_32 for the second term. (Took about 8 minutes
#   to find. >_<)
# Since Python doesn't have unsigned shifts, I didn't think about it.
# I should remember it though. (TODO: Make card)
# Their approach to the xoring is more efficient than mine, at the end.
# (TODO: Make card)
