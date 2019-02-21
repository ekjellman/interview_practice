###
# Problem
###

# Given an NxN matrix of positive and negative integers, write code to find the
# submatrix with the largest possible sum

###
# Work
###
# Questions:
# Size of n?
# Return? (x1, y1, x2, y2)
# Can submatrix be rectangular? (assume yes)

# Approaches:
# Brute force (iterate all UL and DR corners, sum, return best.) O(n**6)
# Calculate all sub-rows and sub-columns like last problem. O(n**5) (since
#   calculating a submatrix is now O(n)
# Can I make it so I can do all the rectangle calcs in O(1)?
#

def best_submatrix(matrix):
  # TODO: Error checking (valid matrix, etc)
  best_sum = float("-inf")
  best_submatrix = None
  for start_row in xrange(len(matrix)):
    for start_col in xrange(len(matrix)):  # nxn
      for end_row in xrange(start_row, len(matrix)):
        for end_col in xrange(start_col, len(matrix)):
          total = compute_submatrix(matrix, start_row, start_col, end_row, end_col)
          if total > best_sum:
            best_sum = total
            best_submatrix = (start_row, start_col, end_row, end_col)
  return best_submatrix

def compute_submatrix(matrix, sr, sc, er, ec):
  total = 0
  for row in xrange(sr, er + 1):
    for col in xrange(sc, ec + 1):
      total += matrix[row][col]
  return total

# Test:
import random
matrix = []
for i in xrange(10):
  matrix.append([random.randint(-20, 20) for _ in xrange(10)])
for row in matrix:
  print "\t".join(str(x) for x in row)
print best_submatrix(matrix)

# Time: 25 minutes (failed)

###
# Mistakes / Bugs / Misses
###
# Only coded n**6 solution, and only thought of n**5 solution.
# At least I got some code down. >_<
# Did not think of n**4 solution. Make a card for the union problem, given you
# have all the values from (0, 0) to (x, y) computed
# Did not think of n**3 solution
