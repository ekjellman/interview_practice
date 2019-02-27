###
# Problem
###

# Take an array of distinct elements and a size, and return a subset of the
# given size of the array elements. All subsets should be equally likely.
# Return the result in input array itself.

###
# Work
###
# Questions:
# What do you mean "return the result in input array itself"? Do you mean
#   don't make a new array for the subset, just put the answer in the first
#   size elements? (Assume yes?)
# Size of the array? Size of size?
#   -- A simple solution is just to shuffle the array, but if the array is large
#      and size is small this may do unnecessary work.

import random
def random_subset(elements, size):
  for i in xrange(min(size, len(elements))):
    swap_index = random.randint(i, len(elements) - 1)
    elements[i], elements[swap_index] = elements[swap_index], elements[i]

# Test
import collections
counts = collections.defaultdict(int)
for i in xrange(10000):
  elements = list("ABC")
  random_subset(elements, 3)
  counts[tuple(elements)] += 1
print counts

counts = collections.defaultdict(int)
for i in xrange(10000):
  elements = list("ABCDEFGHIJ")
  random_subset(elements, 2)
  counts[tuple(elements[:2])] += 1
print counts
print max(counts, key=counts.get)
print min(counts, key=counts.get)

# Time: 7 minutes

###
# Mistakes / Bugs / Misses
###
# Did not think of optimizing for size > len(elements) / 2 by removing elements
#   instead.

