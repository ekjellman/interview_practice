###
# Problem
###

# A robot is in the top left of a grid, and can only go right and down.
# There are some cells that are "off limits"
# Find a path from the top left to the bottom right.

###
# Work
###
# Size of the grid?
# How to return the path? (Assume a string with Rs and Ds is sufficient)
# How to specify off limits cells? (However you want)

def find_path(r, c, off_limits, y=0, x=0, cache=None):
  if y == r and x == c:
    return ""
  if cache is None:
    cache = {}
  if (y, x) in off_limits:
    return None
  if (y, x) in cache:
    return cache[(y, x)]
  result = None
  if y + 1 <= r:
    down_path = find_path(r, c, off_limits, y+1, x, cache)
    if down_path is not None:
      result = "D" + down_path
  if result is None and x + 1 <= c:
    right_path = find_path(r, c, off_limits, y, x+1, cache)
    if right_path is not None:
      result = "R" + right_path
  cache[(y, x)] = result
  return result

print find_path(2, 6, set()), "DDRRRRRR"
off_limits = set([(0, 3), (1, 3), (2, 3)])
print find_path(2, 6, off_limits), "None"
off_limits = set([(1, 3), (2, 3)])
print find_path(2, 6, off_limits), "RRRRDDRR"

# Time: 13 minutes

###
# Mistakes / Bugs / Misses
###
# Lines 28, 30, and 32 were using not x instead of x is not None, but "" is
#   a valid result
