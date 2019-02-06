###
# Problem
###

# Given two lists of ints, find a pair of values (one from each) that you can
# swap to give the two arrays the same sum.

# Ex: [4, 1, 2, 1, 1, 2], [3, 6, 3, 3] outputs (1, 3)

###
# Work
###
# Questions:
# Size of lists? (Assume memory not an issue)
# What if multiple solutions? (Any solution is fine)
# What if no solutions? (None is fine)

def sum_swap(a, b):
  a_sum = sum(a)
  b_sum = sum(b)
  if (b_sum - a_sum) % 2 != 0: return None
  search_diff = (b_sum - a_sum) / 2
  a_set = set(a)
  b_set = set(b)
  for number in b_set:
    if number - search_diff in a_set:
      return (number - search_diff, number)
  return None

# Tests:
print sum_swap([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]), "(1, 3)"
print sum_swap([1, 1, 1, 1, 1], [2, 3]), "None"
print sum_swap([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), "(1, 1)"
print sum_swap([1, 2, 3, 4, 5], [1, 2, 3, 4]), "None"
print sum_swap([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]), "(3, 6) or diff of 3"

# Time: 7 minutes
# If we can't make sets, we could sort and binary search

###
# Mistakes / Bugs / Misses
###
# Didn't think about just iterating through sorted lists

