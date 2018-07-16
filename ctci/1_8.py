###
# Problem
###

# Write an algorithm that, if an element in an MxN matrix is 0, its
# entire row and column are set to 0.

###
# Work
###

# Questions:
# Modify matrix in-place? (Assume yes)
# Non-ragged matrix? (Assume non-ragged)
# Input is a matrix of ints? (Assume yes)
# Optimize for space? (Assume yes)

def set_zeros(matrix):
  column_zero = False
  row_zero = False
  for cell in matrix[0]:
    if cell == 0:
      row_zero = True
      break
  for cell_index in xrange(len(matrix)):
    if matrix[cell_index][0] == 0:
      column_zero = True
      break
  for row in xrange(1, len(matrix)):
    for col in xrange(1, len(matrix[row])):
      if matrix[row][col] == 0:
        matrix[row][0] = 0
        matrix[0][col] = 0
  for row in xrange(1, len(matrix)):
    if matrix[row][0] == 0:
      for col in xrange(1, len(matrix[row])):
        matrix[row][col] = 0
  for col in xrange(1, len(matrix[0])):
    if matrix[0][col] == 0:
      for row in xrange(1, len(matrix)):
        matrix[row][col] = 0
  if column_zero:
    for row in xrange(len(matrix)):
      matrix[row][0] = 0
  if row_zero:
    for col in xrange(len(matrix[0])):
      matrix[0][col] = 0

test_matrix = [[0, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1]]

for row in test_matrix:
  print row

set_zeros(test_matrix)

print

for row in test_matrix:
  print row

# Test cases (Did not save all of them, modified test_matrix)
# Basic 0 in the middle case
# Multiple 0s in row and column
# 0s in first row and first column
# 0 in the upper left corner

# Time: 15 minutes

###
# Mistakes / Bugs / Misses
###

# -- Did not think of questions before starting the problem
# -- Had wrong xrange in 43 and 46, left upper corner as a 1
# -- Did not consider making a function to zero out row and column
