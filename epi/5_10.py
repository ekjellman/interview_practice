###
# Problem
###

# Given a function that randomly returns 0 or 1, write a function that generates
# a random number between [a, b] inclusive with equal probability

###
# Work
###
# Questions: are a and b non-negative? (Assume no)

import random  # for the 0-1

def coin_flip():
  if random.random() > .5: return 0
  return 1

def random_integer(a, b):
  if a == b: return a
  a, b = min(a, b), max(a, b)
  return a + random_int_from_zero(b - a)

def random_int_from_zero(b):
  while True:
    factor = 1
    result = 0
    while b >= factor:
      result += coin_flip() * factor
      factor <<= 1
    if result <= b: return result

# Test:
import collections
print "3-10 test"
c = collections.Counter(random_integer(3, 10) for _ in xrange(10000))
print c
print "-10 to 8 test"
c = collections.Counter(random_integer(-10, 8) for _ in xrange(10000))
print c
print "15 to 6 test"
c = collections.Counter(random_integer(15, 6) for _ in xrange(10000))
print c

# Time: 12 minutes

###
# Mistakes / Bugs / Misses
###
