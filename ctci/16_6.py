###
# Problem
###

# Given two arrays, compute the pair of values (one in each array) with
# the smallest, non-negative difference. Return the difference.

###
# Work
###
# Questions:
# If the difference is non-negative, do we always mean a value in A will
# be greater than a value in B? (Assume yes?)
# What to do if there is no such difference? (Returning None is fine)
# Can we modify the arrays? (Assume yes)

def smallest_difference(a, b):
  a.sort()
  b.sort()
  best_diff, best_pair = float("inf"), None
  index_a, index_b = 0, 0
  while index_a < len(a) and index_b < len(b):
    if a[index_a] >= b[index_b]:
      diff = a[index_a] - b[index_b]
      if diff < best_diff:
        best_diff, best_pair = diff, (a[index_a], b[index_b])
      index_b += 1
    else:
      index_a += 1
  return best_pair

print smallest_difference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]), "11 8"
print smallest_difference([9], [18]), "None"
print smallest_difference([18], [9]), "18 9"
print smallest_difference([], []), "None"
print smallest_difference([3], []), "None"
print smallest_difference([], [4]), "None"

# Time: 9 minutes

###
# Mistakes / Bugs / Misses
###
# Incremented the wrong indices at 27 and 29
# She wanted to find the pair with the minimum absolute difference, which
# would be solved similarly
