###
# Problem
###

# Write a function that takes as input an n x n 2D array, and rotates it 90
# degress clockwise.


###
# Work
###
# Questions:
# Size of the array? (assume fits in memory)
# In-place? (assume yes)
# n even / odd or both? (assume both)

def rotate(matrix):
  n = len(matrix)
  for x in xrange((n + 1) / 2):
    for y in xrange(n / 2):
      ny = x
      nx = n - y - 1
      storage = matrix[y][x]
      for i in xrange(4):
        matrix[ny][nx], storage = storage, matrix[ny][nx]
        ny, nx = nx, n - ny - 1

# Tests:
matrix = [[1, 1, 2, 2],
          [1, 1, 2, 2],
          [3, 3, 4, 4],
          [3, 3, 4, 4]]
rotate(matrix)
for row in matrix:
  print row
print

matrix = [[1, 1, 1, 2, 2],
          [1, 1, 1, 2, 2],
          [3, 3, 5, 2, 2],
          [3, 3, 4, 4, 4],
          [3, 3, 4, 4, 4]]

rotate(matrix)
for row in matrix:
  print row

# Time: 16 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't think about a system where you just store whether a matrix is rotated
# and don't change the original, just return rotated pixels when ask.
