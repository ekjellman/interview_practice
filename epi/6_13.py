###
# Problem
###

# Write a program that takes as input size k, and then maintains a sample of
# size k of items provided to it.

###
# Work
###
# Questions:
# Types of items, size of k, how many items are we expecting, use cases, etc.
# I mean, this question is basically build a reservoir sampler. >_<


import random

class RandomSample(object):
  def __init__(self, k):
    self.k = k
    self.sample = []
    self._count = 0

  def offer(self, item):
    self._count += 1
    if len(self.sample) < self.k:
      self.sample.append(item)
    else:
      replace_index = random.randint(0, self._count - 1)
      if replace_index < self.k:
        self.sample[replace_index] = item

# Test:
rs = RandomSample(100)
for i in xrange(1000000):
  rs.offer(i)
print sorted(rs.sample)

# Time: 6 minutes

###
# Mistakes / Bugs / Misses
###
