###
# Problem
###

# Given two arrays, one shorter (with distinct elements) and one longer, find
# the shortest subarray in the longer array that contains all the elements in
# the shorter array. The items can appear in any order.


###
# Work
###
# Questions:
# Lengths of shorter and longer?
# Returns? (the start, end indices)
# What if there are multiple equal subsequences? (return any)
# What if it isn't in there? (return None)

import collections

def shortest_ss(shorter, longer):
  shorter_set = set(shorter)
  best = None
  start_index = 0
  end_index = -1
  contained = collections.Counter()
  while end_index + 1 < len(longer) or len(contained) == len(shorter_set):
    if len(contained) == len(shorter_set):
      # Remove first element in subarray
      item = longer[start_index]
      if item in shorter_set:
        assert item in contained
        contained[item] -= 1
        if contained[item] == 0:
          del contained[item]
      start_index += 1
    else:
      end_index += 1
      item = longer[end_index]
      if item in shorter_set:
        contained[item] += 1
    if len(contained) == len(shorter_set):
      if best is None or (end_index - start_index) < (best[1] - best[0]):
        best = (start_index, end_index)
  return best

# Test
print shortest_ss((1, 5, 9), (7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7))
print (7, 10)
print shortest_ss((1, 2, 3), (7, 7, 7, 1, 2, 3))
print (3, 5)
print shortest_ss((1, 2, 3), (7, 7, 7, 1, 2, 4))
print None
print shortest_ss((1, 2, 3), (1, 2, 3, 1, 2, 4))
print (0, 2)
print shortest_ss((1, 2, 4), (1, 2, 3, 1, 2, 4))
print (3, 5)

# Time: 17 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't think of 16-17 edge cases until coding.
# forgot colon at 42
# Forgot best is None case at 43
# Off by one at 27 led to IndexError

# Puzzler question:
# ... am I missing something in this problem? Her solution in O(B log S) using
# a heap, and mine is just O(B) (O(1) work for each element in the B array,
# possibly twice. I feel like my analysis must be wrong here? Or does my
# solution not find the best answer?
