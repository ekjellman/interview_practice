###
# Problem
###

# Given a square matrix where every pixel is black or white. Design an algorithm
# to find the maximum subsquare such that all four borders are filled with
# black pixels

###
# Work
###
# Size of matrix?
# Input format? (2d list of 0s and 1s)
# Output? (x1, y1, size) tuple
# What if no answer? (None is fine)

# Approaches:
# Brute force: Start with each UL corner, and try to expand the square until
# it is no longer a square. O(n**5)? 2 for the xy, 2 for the square checking, 1
# for n squares.
# Less brute force: Each time we expand our square, only check the relevant row
#   and column we expand. Now each square takes O(n) to check, so O(n**4)
# Make a dictionary of uninterrupted rows and columns. For each row and column
# do a worst-case O(n**2) pass to say "in this column, we have the uninterrupted
# rows (x, y), (x, y2)...". Then, when we do our checking, for each square we
# have to do O(1) work. O(n**3) to make the dictionary and to check the squares.
# That's the best I can come up and still have time to code, so let's try it.

def largest_square(matrix):
  # TODO: Error checking (assumes rectangular matrix)
  row_set = set()
  col_set = set()
  # TODO: Break out into functions
  for i, row in enumerate(matrix):
    for start in xrange(len(row)):
      for end_index in xrange(start, len(row)):
        if row[end_index] == 1:
          row_set.add((i, start, end_index))
        else:
          break

  for column_index in xrange(len(matrix[0])):
    for start in xrange(len(matrix)):
      for end in xrange(start, len(matrix)):
        if matrix[end][column_index] == 1:
          col_set.add((column_index, start, end))
        else: break

  best = None
  best_size = -1

  for start_row in xrange(len(matrix)):
    for start_col in xrange(len(matrix[0])):
      for inc in xrange(0, min(len(matrix), len(matrix[0]))):
        if in_matrix(matrix, start_row + inc, start_col + inc):
          if ((start_row + inc, start_col, start_col + inc) in row_set and
              (start_col + inc, start_row, start_row + inc) in col_set):
            if inc > best_size:
              best_size = inc
              best = (start_row, start_col, best_size + 1)
        else:
          break
  return best

def in_matrix(matrix, row, col):
  return row >= 0 and col >= 0 and row < len(matrix) and col < len(matrix[0])

# Test:
matrix = [[0, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 1, 1, 1, 1, 0, 0],
          [0, 0, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 1, 1, 1, 1, 0],
          [0, 0, 0, 1, 1, 1, 1, 0],
          [1, 1, 0, 1, 1, 1, 1, 0],
          [1, 1, 0, 1, 1, 1, 0, 0]]
print largest_square(matrix), (2, 3, 4)


# Time: 25 minutes.

###
# Mistakes / Bugs / Misses
###
# Did not think of None question until coding
# Changed output after coding start (from x1 y1 x2 y2)
# Missed colon on 53.
# Messed up indent on line 63
# Had end instead of end_index on 37
# Had best_size instead of best_size + 1 on 60. (inclusive)
# I am not 100% sure this is working correctly, I only have the one test.
# Her preprocessing solution is different than mine, and I think more elegant.
# It makes a matrix saying how many more black cells down and right there are.

