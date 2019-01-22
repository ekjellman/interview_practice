###
# Problem
###

# Given a sorted array of n integers that has been rotated some number of times,
# write code to find an element in the array. The array was sorted in
# increasing order.

###
# Work
###

# Questions:
# Duplicate entries?
# Might the array be unrotated?
# Size of the array?
# What is the return? (Assume position in the array)

# In Python, if I were actually presented with this, I would likely still use
# the O(n) method unless the array were gigantic. But we're looking for the
# O(log n) solution, so let's get to it.

def find_rotated(items, element):
  if items[-1] > items[0]:
    start_point = 0  # Array unrotated
  # binary search for start point
  low = 0
  high = len(items) - 1
  while high > low:
    mid = (low + high) / 2
    if items[mid] > items[0]:
      low = mid + 1
    else:
      high = mid

# Time: 25 minutes (failed)

###
# Mistakes / Bugs / Misses
###
# Need to practice writing binary search. >_< I also spent a lot of time
# grappling with how this is a modification of binary search.
# STUDY THIS PROBLEM (TODO)
