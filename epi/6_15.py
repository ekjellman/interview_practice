###
# Problem
###

# Write a program that takes as input a positive integer n and a size k <= n and
# returns a size-k subset of [0, 1, 2, ..., n-1]. The subset should be
# represented as an array.

###
# Work
###
# Questions:
# Relative sizes of n and k
# What am I trying to minimize here? Space usage? Calls to random number gen?

# Approaches:
# -- Make a list of size n, shuffle the first k elements
# -- Generate a permutation number, create that permutation of size k
# -- Make an empty list, and start generating numbers from 0-(n-1), add them
#    if they're not in the list.

# Which approach I'd take depends on what we expect the relative sizes of n
# and k to be, and what we're trying to optimize.

# Since I haven't written it in a previous problem so far this chapter, I'll
# go with the third one.

import random
def random_subset(n, k):
  # TODO: Error check n, k
  picked = set()   # could skip this, but at a time cost
  subset = []
  while len(subset) < k:
    next_num = random.randint(0, n-1)
    if next_num not in picked:
      subset.append(next_num)
      picked.add(next_num)
  return subset

# Test
import collections
counts = collections.defaultdict(int)
for i in xrange(10000):
  ss = tuple(random_subset(5, 3))
  counts[ss] += 1
for ss in counts:
  print ss, counts[ss]
print len(counts)

# Time: 6 minutes

###
# Mistakes / Bugs / Misses
###
# Make card for their approach. (TODO):
# Have a hashtable where the key is an index in the array, and the value is
# the value at that index. The key is, for all keys not in the hashtable, the
# value is the key. So at the start, say n is 1000. A[0] = 0, A[1] = 1, ...
# up to A[1000] = 1000, but none of those entries are in the hashtable.
# Say then, for the first element you randomly pick 55. If you had the full list
# you would swap 55 into element 0, but here you set A[0] = 55, and A[55] = 0,
# and now your hashtable has 2 elements in it. Continue until you've done the
# k positions you want.
# This ends up taking O(k) space, since at most you'll have 2k entries in the
# hashtable. It's a little unintuitive, since you tend not to use hashtables for
# arrays, but in this case the entries we want could be sparse.
