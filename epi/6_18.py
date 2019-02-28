###
# Problem
###

# Given an nxn 2D array, return its spiral ordering.

# Ex:
#  1 2 3
#  4 5 6
#  7 8 9
#  -> [1 2 3 6 9 8 7 4 5]

###
# Work
###
# Questions:
# Extensibility? (nxm? Size?)
# O(n) space ok? (Going to try to do it as a generator instead)

def spiral_ordering(matrix):
  # TODO: error checking
  layer = 0
  while layer <= len(matrix) / 2:
    # right
    for x in xrange(layer, len(matrix[0]) - layer):
      yield matrix[layer][x]
    # down
    for y in xrange(layer + 1, len(matrix) - layer):
      yield matrix[y][len(matrix) - layer - 1]
    # left
    for x in xrange(len(matrix[0]) - layer - 2, -1 + layer, -1):
      yield matrix[len(matrix) - layer - 1][x]
    # up
    for y in xrange(len(matrix) - layer - 2, -1 + layer + 1, -1):
      yield matrix[y][layer]
    layer += 1

# Tests:
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

print [x for x in spiral_ordering(matrix)]
print "1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10"

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print [x for x in spiral_ordering(matrix)]
print "1 2 3 6 9 8 7 4 5"


# TODO: There is a numerical pattern we can exploit if we know the
#       matrix is numbered the way these have been, but I don't think there's
#       a guarantee of that. We COULD use that number as an index into the 2D
#       array, but I don't think that code is particularly cleaner.

# Time: 15 minutes

###
# Mistakes / Bugs / Misses
###
# Missed a colon at 23
# Off by one error in bounds at 31 and 34
# Their ordering is a little more elegant, the idea of, instead of taking top,
# then right, then bottom, then left strips, of uneven sizes, look at the
# strips like this:
#  xxxy
#  w..y
#  w..y
#  wzzz
# This should make the loops more uniform
