###
# Problem
###

# Design an algorithm to find all pairs of integers within an array which
# sum to a specified value.

###
# Work
###
# Questions:
# Output? (Assume list of tuples)
# Duplicates? (Assume one of each)
# Additional space ok? (Assume yes)
# Can you use a number multiple times? (Assume no)

import collections

def pair_sum(numbers, total):
  num_set = collections.Counter(numbers)
  pairs = []
  for num in num_set:
    if total - num in num_set and num >= total - num:
      if total - num != num:
        pairs.append((num, total - num))
      else:
        if num_set[num] >= 2:
          pairs.append((num, num))
  return pairs

# Tests
print pair_sum((1, 2, 3, 4, 5, 6), 0), "[]"
print pair_sum((1, 2, 3, 4, 5, 6), 7), "[(4, 3), (5, 2), (6, 1)]"
print pair_sum((1, 2, 3, 4, 5, 6), 10), "[(6, 4)]"
print pair_sum((1, 2, 3, 4, 5, 5, 6), 10), "[(6, 4), (5, 5)]"

# Time: 7 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't think of last case / question until writing tests
# Didn't think of sorted array idea (although the additional space question was
#   leading that way)
