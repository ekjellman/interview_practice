###
# Problem
###

# Numbers are generated and passed to a method. Write a program to find and
# maintain the median value as new values are generated

###
# Work
###
# Questions:
# How many numbers? (If it's a small number, sorting and returning the median
#   on demand is clean code and still efficient)
#   -- If it's really large, my solution might not work, especially if the
#      generation is uneven
# Interface? Use cases?
# Which median do you want, particularly for even numbers of values?
#   Left? Average? Both values? (Assuming either median value is ok)
# Unique values? (Assume no)

import heapq

class MedianKeeper(object):
  def __init__(self):
    self.median = None
    # Heaps
    self.lesser = []  # max heap of lesser values.
                      # negated because python heaps are min heaps
    self.greater = []  # min heap of greater values

  def add(self, value):
    if self.median is None:
      self.median = value
    else:
      if value > self.median:
        heapq.heappush(self.greater, value)
      else:
        heapq.heappush(self.lesser, -value)
      self.adjust_median()

  def adjust_median(self):
    if abs(len(self.lesser) - len(self.greater)) <= 1: return
    if len(self.lesser) > len(self.greater):
      heapq.heappush(self.greater, self.median)
      self.median = -heapq.heappop(self.lesser)
    else:
      heapq.heappush(self.lesser, -self.median)
      self.median = heapq.heappop(self.greater)

# Test:
values = [5, 4, 1, 6, 3, 2, 8, 10, 9, 7, 11]
mk = MedianKeeper()
for value in values:
  mk.add(value)
print "6:", mk.median


values = [12, 5, 4, 1, 6, 3, 2, 8, 10, 9, 7, 11]
mk = MedianKeeper()
for value in values:
  mk.add(value)
print "6 or 7:", mk.median

import random
for i in xrange(10):
  values = [random.randint(0, 1000) for _ in xrange(100)]
  mk = MedianKeeper()
  for value in values:
    mk.add(value)
  values.sort()
  print values[49:51], mk.median

# Time: 21 minutes

###
# Mistakes / Bugs / Misses
###
# I looked up Python's heap data structure. I should have a card from last time.
# Forgot colon on line 31
# Forgot - in line 47
# This is a touch sloppy. I'm not making one particular heap always slightly
# larger. This could be fixed in adjust_median.
