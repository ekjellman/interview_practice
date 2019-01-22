###
# Problem
###

# Given an mxn matrix in which each row and each column is sorted in ascending
# order, write a method to find an element

###
# Work
###

# Questions:
# Size of m and n? (If small enough, just use a full scan, or a log n in each
#   row scan)
# Return type? (Assumn row, col of element)
# Can we assume unique elements? (Assume no)
# What do we do if the element doesn't exist?

# Approaches:
# Full scan (O(mn))
# Binary search in each row (O(n log m) or (m log n))
# Recursive scan of three quadrants of matrix.

def matrix_search(matrix, element, min_row=None, max_row=None,
                                   min_col=None, max_col=None):
  if min_row is None:
    min_row = 0
    max_row = len(matrix) - 1
    min_col = 0
    max_col = len(matrix[0]) - 1  # Assumes rectangular matrix
  print min_row, max_row, min_col, max_col
  if min_row == max_row and min_col == max_col:
    if matrix[min_row][min_col] == element:
      return (min_row, min_col)
    else:
      return None
  mid_row = (min_row + max_row) / 2
  mid_col = (min_col + max_col) / 2
  mid_element = matrix[mid_row][mid_col]
  if mid_element == element:
    return (mid_row, mid_col)
  elif mid_element > element:
    result = matrix_search(matrix, element, min_row, mid_row, min_col, mid_col)
    if result: return result
  else:
    result = matrix_search(matrix, element, mid_row, max_row, mid_col, max_col)
    if result: return result
  result = matrix_search(matrix, element, min_row, mid_row, mid_col, max_col)
  if result: return result
  result = matrix_search(matrix, element, mid_row, max_row, min_col, mid_col)
  if result: return result
  return None

matrix = [[0, 2, 4, 6, 8],
          [10, 12, 14, 16, 18],
          [20, 22, 24, 26, 28],
          [30, 32, 34, 36, 38]]

for i in xrange(-1, 40):
  print i, matrix_search(matrix, i)

# Time: 25 minutes (FAILED)

###
# Mistakes / Bugs / Misses
###
# Forgot to ask what we should do if the element doesn't exist. AGAIN.
# This recurses infinitely. I found that the problem is that I'm including
# a middle row/col in the recursion that I don't need to, but I couldn't work
# out exactly where the +1/-1s should go before running out of time. I think the
# real answer is to not have the two quadrants I always search outside of the
# if statement.

# In Gayle's write-up, she points out that I only need to search two areas
# instead of three. Whoops.
