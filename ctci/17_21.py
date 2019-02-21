###
# Problem
###

# Design an algorithm to compute the volume of water a bar graph would hold if
# water was poured in from the top.

# i.e.

"""

          X
          X         X
    X     X         X
    X     X     X   X
    X     X     X   X
    X     X     X   X   X
0 0 4 0 0 6 0 0 3 0 5 0 1 0 0 0
      4 4   5 5 2 5     1

"""
# Output: 26 (4 + 4 + 5 + 5 + 2 + 5 + 1)

###
# Work
###
# Questions:
# Size of histogram?
# Size of bars?
# Don't count bars as water? (Assume correct)
# No water at edges? (Assume correct)
# Overflow concerns in Java (no pun intended)

def volume(histogram):
  left_maxs = [0] * len(histogram)
  current_max = 0
  for i, value in enumerate(histogram):
    current_max = max(value, current_max)
    left_maxs[i] = current_max
  current_max = 0
  water = 0
  for i in xrange(len(histogram) - 1, -1, -1):
    current_max = max(histogram[i], current_max)
    water += min(current_max, left_maxs[i]) - histogram[i]
  return water

# Tests:
print "26", volume((0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0))
print "0", volume((0, 0, 0, 3, 0, 0, 0))
print "6", volume((0, 0, 2, 0, 0, 0, 5, 0))
print "6", volume((0, 0, 5, 0, 0, 0, 2, 0))

# TODO: In a non-worst case, you could save some space using a stack instead of
#       a list for left_maxs.
# Time: 9 minutes

###
# Mistakes / Bugs / Misses
###
# Looked up if there was a reverse enumerate.

